import json
from urllib.parse import quote
from urllib.request import urlopen

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from welfare.froms import WelfareForm
from welfare.models import Welfare


@login_required
def welfare(request, index=''):
    if request.method=='GET':
        if not index:
            return render(request, 'welfare/welfare.html', {'welfareForm':WelfareForm()})
        #save finish
        try:
            welfare = Welfare.objects.get(id=index)
        except:
            messages.success(request, '無此幫助')
            return render(request, 'welfare/welfare.html')
        return render(request, 'welfare/welfare.html', {'welfare':welfare})
    #POST
    welfareForm = WelfareForm(request.POST)
    if not welfareForm.is_valid():
        return render(request, 'welfare/welfare.html', {'welfareForm': welfareForm})
    welfare = welfareForm.save(commit=False)
    welfare.user = request.user
    
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address='+quote(welfare.address)+'&sensor=false&language=zh-tw'
    content = urlopen(url).read().decode('utf-8')
    jsonMessage = json.loads(content)
    location = jsonMessage['results'][0]['geometry']['location']
    welfare.lat = location['lat']
    welfare.lng = location['lng']
    
    welfare.save()
    
    messages.success(request, '填寫成功')
    return redirect(reverse('welfare:welfareIndex', args=(str(welfare.id),)))