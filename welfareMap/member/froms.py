from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    username = forms.CharField(label='帳號')
    password = forms.CharField(label='密碼', widget=forms.PasswordInput)
    password2 = forms.CharField(label='確認密碼', widget=forms.PasswordInput)
    first_name = forms.CharField(label='暱稱')
    
    
    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'first_name')
    
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password!=password2:
            raise forms.ValidationError(' 密碼與確認密碼錯誤')
        return password2