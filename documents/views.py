from django.shortcuts import render
from user.models import PhysicalUser, Address
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
            print(form_data)
        return HttpResponse('asdasdas')
   #
   # type_registration = models.CharField(max_length=200 , choices=TYPE_CHOICES , verbose_name='Вид реєстрації')
   #  property_list_number  = models.IntegerField(verbose_name='Номер запису про право власності')
   #  ownership  = models.CharField(max_length=100 , verbose_name='Форма власності' , choices=OWNER_SHIP_CHOICES)
   #  common_property_type = models.CharField(max_length=100 , verbose_name='Форма власності' , choices=COMMON_PROPERTY_CHOICES)
   #  object_type = models.CharField(max_length=100 , verbose_name='Тип обьекта', choices=OBJECT_TYPE_CHOICES)
   #  register_number  = models.IntegerField(verbose_name='Реєстраційний номер')
   #  address = models.ForeignKey(Address , verbose_name="Адрес" , on_delete=models.CASCADE)
   #  user = models.ForeignKey(PhysicalUser , on_delete=models.CASCADE , default=None)




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