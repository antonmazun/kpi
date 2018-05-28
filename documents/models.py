from django.db import models
from user.models import Address
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

class StatementStateRegistration(models.Model):
    type_registration = models.CharField(max_length=200 , choices=TYPE_CHOICES , verbose_name='Вид реєстрації')
    property_list_number  = models.IntegerField(verbose_name='Номер запису про право власності')
    ownership  = models.CharField(max_length=100 , verbose_name='Форма власності' , choices=OWNER_SHIP_CHOICES)
    common_property_type = models.CharField(max_length=100 , verbose_name='Форма власності' , choices=COMMON_PROPERTY_CHOICES)
    object_type = models.CharField(max_length=100 , verbose_name='Тип обьекта', choices=OBJECT_TYPE_CHOICES)
    register_number  = models.IntegerField(verbose_name='Реєстраційний номер')
    address = models.ForeignKey(Address , verbose_name="Адрес" , on_delete=models.CASCADE)



