from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def about(request):
    return render(request, 'about/about.html')

def idea(request):
    return render(request, 'about/idea.html')

def introduction(request):
    return render(request, 'about/introduction.html')


def use(request):
    return render(request, 'about/use.html')

@login_required
def aboutUs(request):
    return render(request, 'about/aboutUs.html')