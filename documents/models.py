from django.db import models
from user.models import Address, PhysicalUser, Registor
from user.models import Address , PhysicalUser


# Create your models here.
TYPE_CHOICES = (
    ('vun' , 'Виникнення'),
    ('prup' , 'Припинення'),
    ('per' , 'Перехід'),
)


OWNER_SHIP_CHOICES = (
    ('private' , 'Приватна'),
    ('state' , 'Державна'),
    ('other_state' , 'власність інших '),
    ('comunal' , 'Комунальна'),
    ('owner_international' , 'Власність міжнародних організацій і юридичних осіб інших держав'),
)

COMMON_PROPERTY_CHOICES  = (
    ('juically_compatible' , 'Спільна сумісна'),
    ('join_partially' , 'Спільна часткова'),
)

OBJECT_TYPE_CHOICES  = (
    ('land_plot' , 'Земельна ділянка'),
    ('non_residential_premises' , 'Не житлове приміщення'),
    ('living_room' , 'житлове приміщення'),
    ('flat' , 'Квартира'),
)

CANCELATION_CHOICES = (
    ('record','Cкасування запису Державного реєстру речових прав на нерухоме майно'),
    ('registration','Cкасування державної реєстрації речових прав на нерухоме майно та їх обтяжень')
)

class StatementStateRegistration(models.Model):
    type_registration = models.CharField(max_length=200 , choices=TYPE_CHOICES , verbose_name='Вид реєстрації')
    property_list_number  = models.IntegerField(verbose_name='Номер запису про право власності')
    ownership  = models.CharField(max_length=100 , verbose_name='Форма власності' , choices=OWNER_SHIP_CHOICES)
    common_property_type = models.CharField(max_length=100 , verbose_name='Форма власності' , choices=COMMON_PROPERTY_CHOICES)
    object_type = models.CharField(max_length=100 , verbose_name='Тип обьекта', choices=OBJECT_TYPE_CHOICES)
    register_number  = models.IntegerField(verbose_name='Реєстраційний номер')
    address = models.ForeignKey(Address , verbose_name="Адрес" , on_delete=models.CASCADE)
    user = models.ForeignKey(PhysicalUser , on_delete=models.CASCADE , default=None)

class ApplicationForCancelation(models.Model):
    type_cancelation = models.CharField(max_length=50, choices=CANCELATION_CHOICES, verbose_name='Вид скасування')
    application_registration_number = models.IntegerField(verbose_name='Реєстраційний номер об’єкта нерухомого майна')
    property_record_number = models.IntegerField(verbose_name='Номер запису про право власності')
    record_number_other_properties_right = models.IntegerField(verbose_name='Номер запису про інше речове право')
    encumbrance_record_number = models.IntegerField(verbose_name='Номер запису про обтяження')
    motgage_record_number = models.IntegerField(verbose_name='Номер запису про іпотеку')
    record_number_nonowner_real_estate = models.IntegerField(verbose_name='Номер запису про взяття на облік  безхазяйного нерухомого майна')
    grounds_for_cancelation = models.CharField(max_length=255, verbose_name='Підстава для скасування')
    user = models.ForeignKey(PhysicalUser, verbose_name='Юзер', on_delete=models.CASCADE)
    #registor = models.ForeignKey(Registor, verbose_name='Реєстратор', on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Дата',auto_now=False, auto_now_add=False)



