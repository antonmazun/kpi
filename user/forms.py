from django.forms import ModelForm
from .models import PhysicalUser , LegalPerson , Address
from django import forms


class PhysicalUserForm(ModelForm):
    class Meta:
        model = PhysicalUser
        # fields = '__all__'
        exclude  = ['id_card' , 'passport_number' , 'passport_serial', 'date_issue' , 'publisher' , 'adress']
        widgets = {
            'password': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
            'date_issue': forms.SelectDateWidget()
        }


class LegalPersonForm(ModelForm):
    class Meta:
        model = LegalPerson
        exclude = ['adress_company']

        widgets = {
            'password_legal': forms.PasswordInput(),
            'password_legal2': forms.PasswordInput(),
        }

class LoginForm(ModelForm):
    class Meta:
        model = PhysicalUser
        fields  = ['login' , 'password']


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'