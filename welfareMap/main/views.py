from django.shortcuts import render
from django.http.response import HttpResponse

# reate your views here.
def main(request):

    return render(request, 'main/main.html')