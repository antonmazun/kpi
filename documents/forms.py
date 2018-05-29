from django.forms import ModelForm
from .models import StatementStateRegistration, ApplicationForCancelation

from django import forms

class StatementStateRegistrationForm(ModelForm):
    class Meta:
        model = StatementStateRegistration
        exclude  = ['user']

class ApplicationForCancelationForm(ModelForm):
    class Meta:
        model = ApplicationForCancelation
        exclude = ['registor','user']


