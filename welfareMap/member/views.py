from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from member.froms import UserForm
from welfare.models import Welfare


# Create your views here.
def member(request):
    return render(request, 'member/member.html')
@login_required
def welfareNum(request):
    welfares = Welfare.objects.filter(user=request.user)
    return render(request, 'member/welfareNum.html', {'welfares':welfares})

@login_required
def supplyNum(request):
    welfares = Welfare.objects.filter(helpUser=request.user)
    return render(request, 'member/supplyNum.html', {'welfares':welfares})

@login_required
def manager(request):
    if request.method=='GET':
        return render(request, 'member/manager.html', {'userForm':UserForm(instance=request.user)})
    #POST
    userForm = UserForm(request.POST, instance=request.user)
    if not userForm.is_valid():
        return render(request, 'member/manager.html', {'userForm': userForm})
    user = userForm.save()
    user.set_password(user.password)
    user.save()
    messages.success(request, '修改成功,請重新登入')
    return redirect('/')

def register(request):
    if request.method=='GET':
        return render(request, 'member/register.html', {'userForm':UserForm()})
    #POST
    userForm = UserForm(request.POST)
    if not userForm.is_valid():
        return render(request, 'member/register.html', {'userForm': userForm})
    user = userForm.save()
    user.set_password(user.password)
    user.save()
    messages.success(request, '註冊成功')
    return redirect(reverse('userLogin:userLogin'))