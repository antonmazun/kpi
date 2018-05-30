from django.shortcuts import render
from .forms import RegistorForm
from .models import Registor
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from documents.models import StatementStateRegistration
# Create your views here.

def registrator_login(request):
    form_registor = RegistorForm()
    if request.method == "GET":
        ctx = {}
        ctx['form_registor'] = form_registor
        return render(request , 'registor_login.html' , ctx)
    elif request.method == 'POST':
        form_registor = RegistorForm(request.POST)
        ctx  = {}
        if form_registor.is_valid():
            form_data = form_registor.cleaned_data
            if form_data['login'] == 'registor':
                try:
                    registrator  = Registor.objects.get(
                        login=form_data['login'],
                        password=form_data['password'],
                    )
                    ctx['registrator'] = registrator
                    ctx['user_registrator'] = True
                    request.session['id_registrator'] = registrator.id
                    return render(request , 'registor.html' , ctx)
                except ObjectDoesNotExist as e:
                    ctx['error_entry'] = True
                    return render(request , 'registor_login.html' , ctx)
            else:
                ctx['error_entry'] = True
                ctx['form_registor'] = form_registor
                return render(request, 'registor_login.html', ctx)


def get_all_register(request):
    ctx = {}
    ctx['user_registrator'] = True
    try:
        all_statement_state_registration = StatementStateRegistration.objects.all()
        ctx['all_statement_state_registration'] = all_statement_state_registration
        return render(request , 'all_statement_state_registration.html', ctx)
    except ObjectDoesNotExist as e:
        ctx['none_statement'] = True
        return render(request, 'all_statement_state_registration.html', ctx)


def get_statement(request , id):
    document = StatementStateRegistration.objects.get(id=id)
    ctx = {}
    ctx['user_registrator'] = True
    if request.method == "GET":
        ctx['document'] = document
        ctx['user_registrator'] = True
        return render(request , 'document.html' , ctx)
    elif request.method == 'POST':
        if 'status' in request.POST:
            status  = request.POST.get('status')
            document.status = status
            document.save()
            return render(request, 'all_statement_state_registration.html', ctx)
