from django.shortcuts import render
from django.http.response import JsonResponse


# Create your views here.
def webService(request):
    return JsonResponse({'a':'b'})