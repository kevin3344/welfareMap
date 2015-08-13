from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib import messages


# reate your views here.
def main(request):
    if not User.objects.all():
        user = User()
        user.username = 'admin'
        user.first_name = '管理員'
        user.set_password('admin')
        user.email = 'admin@admin.admin'
        user.is_staff = True
        user.is_superuser = True
        user.save()
        messages.success(request, '管理者新增成功')
    return render(request, 'main/main.html')