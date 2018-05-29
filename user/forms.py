from django.forms import ModelForm
from .models import PhysicalUser , LegalPerson
from django import forms


class PhysicalUserForm(ModelForm):
    class Meta:
        model = PhysicalUser
        # fields = '__all__'
        exclude  = ['id_card' , 'passport_number' , 'passport_serial', 'date_issue' , 'publisher' , 'adress']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Пароль'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Повторний пароль'}),
            'date_issue': forms.SelectDateWidget(),
            'login': forms.TextInput(attrs={'placeholder': 'Логін'}),
            'first_name': forms.TextInput(attrs={'placeholder': "Ім'я"}),
            'second_name': forms.TextInput(attrs={'placeholder': 'Прізвище'}),
            'middle_name': forms.TextInput(attrs={'placeholder': 'По батькові'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'ipn': forms.TextInput(attrs={'placeholder': 'Індифікаційний номер'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Номер телефону'}),

        }


class LegalPersonForm(ModelForm):
    class Meta:
        model = LegalPerson
        exclude = ['adress_company']

        widgets = {
            'password_legal': forms.PasswordInput(attrs={'placeholder': 'Пароль'}),
            'password_legal2': forms.PasswordInput(attrs={'placeholder': 'Повторний пароль'}),
            'login': forms.TextInput(attrs={'placeholder': 'Логін'}),
        }

class LoginForm(ModelForm):
    class Meta:
        model = PhysicalUser
        fields  = ['login' , 'password']

        widgets = {
            'login': forms.TextInput(attrs={'placeholder': 'Логін'}),
            'password': forms.TextInput(attrs={'placeholder': 'Пароль'}),

        }