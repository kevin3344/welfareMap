from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from welfare.models import Welfare


def search(request):
    address = request.GET.get('address')
    urgent = request.GET.get('urgent')
    helpType = request.GET.get('helpType')
    welfares = Welfare.objects.filter(helpUser__isnull=True)
    if not address and not urgent and not helpType:
        welfares = welfares.order_by('-date')[:100]
        return welfares

    if address:
        print(address)
        welfares = welfares.filter(address__icontains=address)
    if urgent:
        print(urgent)
        welfares = welfares.filter(urgent=urgent)
    if helpType:
        welfares = welfares.filter(helpType=helpType)
    return welfares

@login_required
def supplyMap(request):
    if request.method == 'GET':
        welfares = search(request)
        zoom = 8
        wid = request.GET.get('id')
        try:
            welfare = Welfare.objects.get(id=wid)
        except:
            return render(request, 'supply/supplyMap.html', {'welfares':welfares, 'zoom':zoom})
        
        zoom = 16
        return render(request, 'supply/supplyMap.html', {'welfares':welfares, 'welfare':welfare, 'zoom':zoom})
    #post
    id = request.POST.get('id')
    welfare = Welfare.objects.get(id = id)
    welfare.helpUser = request.user
    welfare.save()
    return redirect('/')

def supplyList(request):
    if request.method == 'GET':
        welfares = search(request)
        return render(request, 'supply/supplyList.html', {'welfares':welfares})
    #post
    id = request.POST.get('id')
    welfare = Welfare.objects.get(id = id)
    welfare.helpUser = request.user
    welfare.save()
    return redirect('/')