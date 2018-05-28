from django.shortcuts import render  ,redirect
from .forms import PhysicalUserForm , LoginForm  , LegalPersonForm
from .models import PhysicalUser
from django.http import  HttpResponse
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
            user =  PhysicalUser.objects.get(login=login ,password=password)
            print(user.id)
            if user:
                request.session['entry_user'] = user.id
                ctx = {}
                ctx['user'] = user
                return render(request , 'menu.html' , ctx)
            else:
                return HttpResponse('sdasdas')
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
    ctx  = {}
    ctx['user'] = user
    if user.passport_number:
        ctx['passport_fields'] = True
    # print(user.passport_number)
    return render(request , 'personal_info.html', ctx)


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


def get_info_dovidky(request , id):
    u  = PhysicalUser.objects.get(id=id)
    ctx  = {}
    ctx['user'] = u
    return render(request , 'get_info_dovidky.html' , ctx)