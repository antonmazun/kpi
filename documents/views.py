from django.shortcuts import render  ,redirect
from user.models import PhysicalUser, Address
from .forms import StatementStateRegistrationForm, ApplicationForCancelationForm
from django.http import HttpResponse
from .models import ApplicationForCancelation
from .forms import StatementStateRegistrationForm
from user.forms import AddressForm
from .models import StatementStateRegistration
from django.http import HttpResponse

# Create your views here.


def all_documents(request):
    id_current_user  = request.session['entry_user']
    # print(id_one)
    u = PhysicalUser.objects.get(id=id_current_user)
    ctx  = {}
    ctx['user'] = u
    return render(request , 'all_document.html', ctx)

def add_statement_state_registration(request):
    id_current_user = request.session['entry_user']
    if request.method == 'GET':
        form  = StatementStateRegistrationForm()
        adress_form  = AddressForm()
        u = PhysicalUser.objects.get(id=id_current_user)
        ctx = {}
        ctx['user'] = u
        ctx['form'] = form
        ctx['adress_form'] = adress_form
        return  render(request , 'statement_state_registration_form.html' ,ctx)
    elif request.method == "POST":
        form  = StatementStateRegistrationForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            user_id  = request.POST.get('user_id')
            u = PhysicalUser.objects.get(id=user_id)
            StatementStateRegistration.objects.create(
                type_registration = form_data['type_registration'],
                property_list_number = form_data['property_list_number'],
                ownership = form_data['ownership'],
                common_property_type = form_data['common_property_type'],
                object_type = form_data['object_type'],
                address = form_data['address'],
                user = u,
                register_number = form_data['register_number'],
            )
        return redirect('/documents/statement_state_registration/')

def add_application_for_cancelation(request, id):
    if request.method == 'GET':
        form = ApplicationForCancelationForm()
        u = PhysicalUser.objects.get(id=id)
        ctx = {}
        ctx['user'] = u
        ctx['form'] = form
        return render(request, 'application_for_cancelation_form.html', ctx)
    if request.method == 'POST':
        id_current_user = request.session['entry_user']
        form = ApplicationForCancelationForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            #print()
            u = PhysicalUser.objects.get(id=id)
            # form['type_cancelation'] = request.POST.get('type_cancelation')
            # form['application_registration_number'] = request.POST.get('application_registration_number')
            # form['property_record_number'] = request.POST.get('property_record_number')
            # form['record_number_other_properties_right'] = request.POST.get('record_number_other_properties_right')
            # form['encumbrance_record_number'] = request.POST.get('encumbrance_record_number')
            # form['motgage_record_number'] = request.POST.get('motgage_record_number')
            # form['record_number_nonowner_real_estate'] = request.POST.get('record_number_nonowner_real_estate')
            # form['grounds_for_cancelation'] = request.POST.get('grounds_for_cancelation')
            ApplicationForCancelation.objects.create(
                type_cancelation=form_data['type_cancelation'],
                application_registration_number=form_data['application_registration_number'],
                property_record_number=form_data['property_record_number'],
                record_number_other_properties_right = form_data['record_number_other_properties_right'],
                encumbrance_record_number = form_data['encumbrance_record_number'],
                motgage_record_number = form_data['motgage_record_number'],
                record_number_nonowner_real_estate = form_data['record_number_nonowner_real_estate'],
                grounds_for_cancelation = form_data['grounds_for_cancelation'],
                user = u,
                date = form_data['date']
            )
            print(form_data)
        return redirect('/documents/application_for_cancelation/' + str(id))


def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            Address.objects.create(
                country = form_data['country'],
                region = form_data['region'],
                city = form_data['city'],
                street = form_data['street'],
                bilding_type = form_data['bilding_type'],
                numberbild = form_data['numberbild'],
                kv = form_data['kv'],
            )
            id_current_user = request.session['entry_user']
            u = PhysicalUser.objects.get(id=id_current_user)
            ctx = {}
            form = StatementStateRegistrationForm()
            ctx['user'] = u
            ctx['form'] = form
            return render(request , 'statement_state_registration_form.html' ,ctx)
