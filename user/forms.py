from django.forms import ModelForm
from .models import PhysicalUser , LegalPerson , Address
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
            'EDRPOU': forms.TextInput(attrs={'placeholder': ' ЄДРПОУ'}),
            'name_company': forms.TextInput(attrs={'placeholder': 'Назва компанії'}),
            'first_name_LeadCompany': forms.TextInput(attrs={'placeholder': "Ім'я засновника компанії"}),
            'last_name_LeadCompany': forms.TextInput(attrs={'placeholder': 'Прізвище засновника компанії'}),
            'tax_number_person': forms.TextInput(attrs={'placeholder': 'Податковий номер'}),
            'middle_name_LeadCompany': forms.TextInput(attrs={'placeholder': 'По батькові засновника компанії'}),

        }

class LoginForm(ModelForm):
    class Meta:
        model = PhysicalUser
        fields  = ['login' , 'password']


        widgets = {
            'login': forms.TextInput(attrs={'placeholder': 'Логін'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Пароль'}),

        }


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

