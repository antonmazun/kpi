from django.db import models

# Create your models here.
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

