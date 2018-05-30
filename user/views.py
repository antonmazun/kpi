from django.shortcuts import render  ,redirect
from .forms import PhysicalUserForm , LoginForm  , LegalPersonForm , AddressForm
from .models import PhysicalUser , Address, Registor
from django.http import  HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from documents.models import StatementStateRegistration
# Create your views here.





def test(request):
    login_form  = LoginForm()
    ctx = {}
    ctx['login_form'] = login_form
    return render(request , 'login.html' ,ctx)


def login(request):
    if request.method == 'POST':
        form =  LoginForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            login = form['login']
            password = form['password']
            if login =='registrator':
                ctx = {}
                registrator = Registor.objects.get(login=login, password=password)
                request.session['id_registor'] = registrator.id
                ctx['user_registrator'] = True
                return  render(request , 'registrator.html' , ctx)
            try:
                user =  PhysicalUser.objects.get(login=login ,password=password)
                request.session['entry_user'] = user.id
                ctx = {}
                ctx['user'] = user
                return render(request , 'menu.html' , ctx)
            except ObjectDoesNotExist as e:
                ctx  = {}
                login_form = LoginForm()
                ctx['login_form'] = login_form
                ctx['object_does_not_exist'] = 'Ви ввели неправильні данні'
                return render(request , 'login.html' , ctx)

        return HttpResponse('error!')

def register(request):
    register_form_psysical = PhysicalUserForm()
    register_form_legal = LegalPersonForm()
    ctx = {}
    ctx['register_form_psysical'] = register_form_psysical
    ctx['register_form_legal'] = register_form_legal
    if request.method == 'GET':
        return render(request , 'register.html' , ctx)
    elif request.method == "POST":
        form = PhysicalUserForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            form['type_user'] = request.POST.get('type_user')
            login = form['login']
            repaat_user  = PhysicalUser.objects.filter(login=login)
            if repaat_user:
                ctx['error_registration'] = 'Такий користувач вже є в системі!'
                # print(repaat_user)
                return render(request , 'register.html' , ctx)
            if "passport_number" and 'passport_serial' and 'passport_date' and 'passport_publisher' and form['type_user']=='psysical_user' in request.POST:
                form['passport_number'] = request.POST.get('passport_number')
                form['passport_serial'] = request.POST.get('passport_serial')
                form['passport_date'] = request.POST.get('passport_date')
                form['passport_publisher'] = request.POST.get('passport_publisher')
                print('С ПАСПОРТОМ!')
                PhysicalUser.objects.create(
                    login=form['login'],
                    password=form['password'],
                    first_name=form['first_name'],
                    second_name=form['second_name'],
                    middle_name=form['middle_name'],
                    phone_number=form['phone_number'],
                    email=form['email'],
                    ipn=form['ipn'],
                    passport_number=form['passport_number'],
                    passport_serial=form['passport_serial'],
                    date_issue=form['passport_date'],
                    publisher=form['passport_publisher'],
                    id_card=form['card']
                )
            card = request.POST.get('card')
            form['card'] = card
            if  card != '' and form['type_user'] == 'psysical_user':
                print('Сюда но не должно!')
                form['passport_number'] = request.POST.get('passport_number')
                form['passport_serial'] = request.POST.get('passport_serial')
                form['passport_date'] = request.POST.get('passport_date')
                form['passport_publisher'] = request.POST.get('passport_publisher')
                form['card'] = request.POST.get('card')
                print(type(form['card']))
                PhysicalUser.objects.create(
                    login=form['login'],
                    password=form['password'],
                    first_name=form['first_name'],
                    second_name=form['second_name'],
                    middle_name=form['middle_name'],
                    phone_number=form['phone_number'],
                    email=form['email'],
                    ipn=form['ipn'],
                    id_card =form['card']
                )
            elif card == ''  and form['type_user'] == 'psysical_user':
                form['passport_number'] = request.POST.get('passport_number')
                form['passport_serial'] = request.POST.get('passport_serial')
                form['passport_date'] = request.POST.get('passport_date')
                form['passport_publisher'] = request.POST.get('passport_publisher')
                PhysicalUser.objects.create(
                    login=form['login'],
                    password=form['password'],
                    first_name=form['first_name'],
                    second_name=form['second_name'],
                    middle_name=form['middle_name'],
                    phone_number=form['phone_number'],
                    email=form['email'],
                    ipn=form['ipn'],
                    passport_number=form['passport_number'],
                    passport_serial=form['passport_serial'],
                    date_issue=form['passport_date'],
                    publisher=form['passport_publisher']
                )
            if form['type_user'] == 'psysical_user' and not "card" in request.POST:
                print('С ПАСПОРТОМ!')

                PhysicalUser.objects.create(
                    login=form['login'],
                    password=form['password'],
                    first_name=form['first_name'],
                    second_name=form['second_name'],
                    middle_name=form['middle_name'],
                    phone_number=form['phone_number'],
                    email=form['email'],
                    passport_number=form['passport_number'],
                    passport_serial=form['passport_serial'],
                    date_issue=form['passport_date'],
                    publisher=form['passport_publisher'],
                    ipn=form['ipn']
                )
            user = PhysicalUser.objects.latest('id')
            request.session['entry_user'] = user.id
            ctx = {
                'user': user,
                'type_user': 'Фізична особа'
            }
        return render(request , 'main.html' , ctx)



def personal_info(request , id):
    user = PhysicalUser.objects.get(id=id)
    if request.method == "GET":
        form_adress = AddressForm()
        ctx  = {}
        ctx['user'] = user
        ctx['form_adress'] = form_adress
        if user.passport_number:
            ctx['passport_fields'] = True
        if user.adress:
            print(user.adress.id)
            adress_user = Address.objects.get(id=user.adress.id)
            ctx['adress_user'] = adress_user
        return render(request , 'personal_info.html', ctx)
    elif request.method == "POST":
        form_adress = AddressForm(request.POST)
        if form_adress.is_valid():
            form_data = form_adress.cleaned_data
            Address.objects.create(
                country = form_data['country'].lower(),
                region = form_data['region'].lower(),
                city = form_data['city'].lower(),
                street = form_data['street'].lower(),
                bilding_type = form_data['bilding_type'].lower(),
                numberbild = form_data['numberbild'],
                kv = form_data['kv']
            )
            adress_for_user  = Address.objects.latest('id')
            print('adress_for_user' , adress_for_user.id)
            user.adress = adress_for_user
            user.save()
            return redirect('/personal-info/' + str(id))



def contact_data(request , id):
    user  = PhysicalUser.objects.get(id=id)
    ctx  = {}
    ctx['user'] = user
    return render(request , 'contact_data.html' , ctx)

def update_contact(request , id):
    if request.method == "POST":
        u = PhysicalUser.objects.get(id=id)
        # print(u)
        u.email  = request.POST.get('new_email')
        print("ntktajy", u.phone_number)
        u.phone_number  = request.POST.get('phone_number')
        u.save()
        ctx  = {}
        ctx['user'] = u
        return redirect('/contact-data/' + str(id))



def menu(request , id):
    u = PhysicalUser.objects.get(id=id)
    ctx  = {}
    ctx['user'] = u
    return render(request , 'menu.html' , ctx)


def change_password(request, id):
    user = PhysicalUser.objects.get(id=id)
    if request.method == 'GET':
        ctx = {}
        ctx['user'] = user
        return render(request,'change_password.html',ctx)
    if request.method == 'POST':
        user = PhysicalUser.objects.get(id=id)
        old_password = request.POST.get('old_password')
        if user.password == old_password:
            if request.POST.get('new_password') == request.POST.get('new_password_2'):
                user.password = request.POST.get('new_password')
                user.save()
                return redirect('/change-password/' + str(id))
            else :
                return HttpResponse('Паролі не співпадають')
        else:
            ctx= {}
            ctx['error_old_password'] = "Ви ввели неправильний пароль"
            ctx['user'] = user
            return render(request , 'change_password.html' ,ctx)




def get_info_dovidky(request , id):
    u = PhysicalUser.objects.get(id=id)
    ctx = {}
    ctx['user'] = u
    if 'get_search' in request.GET:
        get_value_search = request.GET.get('get_search')
        if get_value_search == 'adress_choice':
            form_adress = AddressForm()
            ctx['form_adress'] = form_adress
            return render(request , 'search_adress.html' , ctx)
    return render(request , 'get_info_dovidky.html' , ctx)


def logout(request):
    if request.session['entry_user']:
        del request.session['entry_user']
    return redirect('/')


def previous(request):
    user_id = request.session['entry_user']
    return redirect('/get-info-dovidky/' + str(user_id))

def search_for_adress(request):
    form  = AddressForm(request.GET)
    if form.is_valid():
        form_data  = form.cleaned_data
        country = form_data['country']
        region = form_data['region']
        city = form_data['city']
        street = form_data['street']
        bilding_type = form_data['bilding_type']
        numberbild = form_data['numberbild']
        kv = form_data['kv']
        try:
            result_search = Address.objects.get(
                country=country,
                region=region,
                city=city,
                street=street,
                bilding_type=bilding_type,
                numberbild=numberbild,
                kv=kv
            )
            user_search = PhysicalUser.objects.get(adress=result_search.id)
            ctx = {}
            ctx['result_search'] = result_search
            ctx['user_search'] = user_search
            ctx['user'] = PhysicalUser.objects.get(id=request.session['entry_user'])
            print(request.session['entry_user'])
            return render(request, 's_result_adress.html', ctx)
        except ObjectDoesNotExist as e:
            ctx = {}
            ctx['user'] = PhysicalUser.objects.get(id=request.session['entry_user'])
            ctx['null_result_search'] = True
            ctx['country'] = country
            ctx['region'] = region
            ctx['city'] = city
            ctx['street'] = street
            ctx['bilding_type'] = bilding_type
            ctx['numberbild'] = numberbild
            ctx['kv'] = kv
            return render(request , 's_result_adress.html', ctx)


def get_info(request):
    id_user  = request.session['entry_user']
    user  = PhysicalUser.objects.get(id=id_user)
    ctx  = {}
    try:
        user_document = StatementStateRegistration.objects.filter(user=user)
        ctx['user_document'] = user_document
        return render(request , 'user_document.html' , ctx)
    except ObjectDoesNotExist as e:
        ctx['none_document'] = True
        return render(request, 'user_document.html', ctx)

