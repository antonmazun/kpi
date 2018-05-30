from django.forms import ModelForm
from django import forms
from .models import Registor


class RegistorForm(ModelForm):
    class Meta:
        model = Registor
        fields = ['login' , 'password']

        widgets = {
            'login': forms.TextInput(attrs={'placeholder': 'Логін'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Пароль'}),

        }
