from django.forms import ModelForm
from .models import StatementStateRegistration

from django import forms

class StatementStateRegistrationForm(ModelForm):
    class Meta:
        model = StatementStateRegistration
        exclude  = ['user']



