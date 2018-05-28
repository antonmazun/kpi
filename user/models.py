from django.db import models

# Create your models here.



class Address(models.Model):
    country = models.CharField(max_length=255,verbose_name='country')
    region = models.CharField(max_length=255,verbose_name='region')
    city = models.CharField(max_length=255, verbose_name='city')
    street = models.CharField(max_length=255, verbose_name='street')
    bilding_type = models.CharField(max_length=255,verbose_name='bilding_type')
    numberbild = models.IntegerField(verbose_name='number_bild')
    kv = models.IntegerField(verbose_name='kv')

    def __str__(self):
        return 'Країна {} Місто {} Вулиця {} Номер будинку {}'.format(self.country , self.city , self.street , self.bilding_type)




class PhysicalUser(models.Model):
    login  = models.CharField(max_length=255 , verbose_name ='Логін')
    password = models.CharField(max_length=255 , verbose_name='Пароль')
    password2 = models.CharField(max_length=255 , verbose_name='Потвердите пароль' ,blank=True, null=True)
    first_name = models.CharField(max_length=255 , verbose_name='Ім’я')
    second_name = models.CharField(max_length=255 , verbose_name='Прізвище')
    middle_name = models.CharField(max_length=255 , verbose_name='По батькові')
    phone_number  = models.CharField(max_length=255 , verbose_name='Телефонний номер' , default='')
    email = models.CharField(max_length=255 , verbose_name='E-mail')
    passport_number = models.IntegerField(verbose_name='Номер паспорта', blank=True , null=True)
    passport_serial= models.CharField(max_length=2 , verbose_name='Серія паспорта', blank=True , null=True)
    adress = models.ForeignKey(Address ,verbose_name='Адрес', on_delete=models.CASCADE , blank=True , null=True)
    date_issue = models.DateField(verbose_name='Коли виданий', blank=True , null=True)
    publisher = models.CharField(max_length=255, verbose_name='Ким виданий' , default=None, blank=True , null=True)
    id_card  = models.CharField(max_length=255,verbose_name='id card' , null=True , blank=True)
    ipn = models.CharField(max_length=255 , verbose_name='Ідентифікаціонний код',blank=True , null=True)


    def __str__(self):
        return self.login

class Registor(models.Model):
    login = models.CharField(max_length=255, verbose_name='Логін')
    password = models.CharField(max_length=255, verbose_name='Пароль')
    password2 = models.CharField(max_length=255, verbose_name='Потвердите пароль', default=None)
    first_name = models.CharField(max_length=255, verbose_name='first_name')
    last_name = models.CharField(max_length=255, verbose_name='last name')
    middle_name = models.CharField(max_length=255, verbose_name='middle name')
    tax_number_registrator = models.IntegerField(verbose_name='tax number_registrator')
    passport_number = models.IntegerField(verbose_name='password number')
    passport_serial = models.CharField(max_length=2, verbose_name='passport serial')
    ipn = models.IntegerField(verbose_name='ipn')
    id_card = models.IntegerField(verbose_name='id_card')
    date_issue = models.DateField(auto_now=False)
    publisher = models.CharField(max_length=255, verbose_name='publisher')
    type_document_registrat = models.CharField(max_length=255, verbose_name='type_document_registrat')
    doc_number = models.CharField(max_length=255, verbose_name='doc_number')
    doc_serial = models.CharField(max_length=255, verbose_name='doc_serial')
    date_issue_doc = models.CharField(max_length=255, verbose_name='date_issue_doc')
    publisher_doc = models.CharField(max_length=255, verbose_name='publisher_doc')



class LegalPerson(models.Model):
    login = models.CharField(max_length=255, verbose_name='Логін'  ,default=None)
    password_legal = models.CharField(max_length=255, verbose_name='Пароль')
    password_legal2 = models.CharField(max_length=255, verbose_name='Потвердите пароль', default=None)
    EDRPOU = models.IntegerField(verbose_name='EDRPOU' , default=123213)
    name_company = models.CharField(max_length=255, verbose_name='name company')
    adress_company = models.ForeignKey(Address, on_delete=models.CASCADE , default=None)
    first_name_LeadCompany = models.CharField(max_length=255, verbose_name='first_name')
    last_name_LeadCompany = models.CharField(max_length=255, verbose_name='last_name')
    middle_name_LeadCompany = models.CharField(max_length=255, verbose_name='middle_name')
    tax_number_person = models.IntegerField(verbose_name='tax number')




class Document(models.Model):
    doctype = models.CharField(max_length=255, verbose_name='document type')
    idRegistrator = models.ForeignKey(Registor, on_delete=models.CASCADE)
    id_physical = models.ForeignKey(PhysicalUser, on_delete=models.CASCADE , default=None)
    id_legal = models.ForeignKey(LegalPerson, on_delete=models.CASCADE , default=None)
    status = models.CharField(max_length=255, verbose_name='status')