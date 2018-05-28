from django.shortcuts import render
from user.models import PhysicalUser, Address
from .forms import StatementStateRegistrationForm
from django.http import HttpResponse
# Create your views here.


def all_documents(request ):
    id_current_user  = request.session['entry_user']
    # print(id_one)
    u = PhysicalUser.objects.get(id=id_current_user)
    ctx  = {}
    ctx['user'] = u
    return render(request , 'all_document.html', ctx)

def add_statement_state_registration(request , id):
    if request.method == 'GET':
        form  = StatementStateRegistrationForm()
        u = PhysicalUser.objects.get(id=id)
        ctx = {}
        ctx['user'] = u
        ctx['form'] = form
        return  render(request , 'statement_state_registration_form.html' ,ctx)
    elif request.method == "POST":
        form  = StatementStateRegistrationForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            print(form_data)
        return HttpResponse('asdasdas')