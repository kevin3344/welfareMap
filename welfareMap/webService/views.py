from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def webService(request):
    return JsonResponse({'a':'b'})


@csrf_exempt
def register(request):
    if request.method=='POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            name = request.POST.get('name')
            user = User()
            user.username = username
            user.first_name = name
            user.set_password(password)
            user.save()
        except:
            return JsonResponse({'error':True})
        return JsonResponse({'error':False})
    
@csrf_exempt
def getUser(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        userDic = {'username':username, 'password':password,
                   'name':user.first_name}
    return JsonResponse(userDic)
    