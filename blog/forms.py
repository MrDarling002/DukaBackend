from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Application


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', required=True, widget=forms.TextInput(attrs={}))
    password1 = forms.CharField(label='Пароль', required=True, widget=forms.PasswordInput(attrs={}))
    password2 = forms.CharField(label='Пароль2', required=True, widget=forms.PasswordInput(attrs={}))
    email = forms.CharField(label='E-mail', required=True, widget=forms.TextInput(attrs={}))
    first_name = forms.CharField(label='Имя', required=True, widget=forms.TextInput(attrs={}))
    last_name = forms.CharField(label='Фамилия', required=True, widget=forms.TextInput(attrs={}))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", 'password2', "username")
        
    def save(self,commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            return user

class ApplicationForm(forms.ModelForm):
    class Meta:
        model=Application
        fields=['something']