from django.shortcuts import render
from member.froms import UserForm

# Create your views here.
def member(request):
    return render(request, 'member/member.html')

def register(request):
    context = {'userForm':UserForm()}
    print(UserForm())
    return render(request, 'member/register.html', context)