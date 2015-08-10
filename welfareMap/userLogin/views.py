from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.http.response import HttpResponseRedirect
from django.shortcuts import render


def userLogout(request):
    logout(request) 
    return HttpResponseRedirect('/')

def userLogin(request):
    template = 'userLogin/userLogin.html'
    context = {'loginForm':True}
    if request.method=='POST':  # Logout or show the login form
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, '登入成功')
            return HttpResponseRedirect('/')
        else:
            messages.error(request, '登入失敗')
    return render(request, template, context)

