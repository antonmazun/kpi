from django.shortcuts import render
from user.models import PhysicalUser
# Create your views here.


def all_documents(request , id_one):
    print(id_one)
    u = PhysicalUser.objects.get(id=id_one)
    ctx  = {}
    ctx['user'] = u
    return render(request , 'all_document.html', ctx)

def add_statement_state_registration(request , id):
    u = PhysicalUser.objects.get(id=id)
    ctx = {}
    ctx['user'] = u
    return  render(request , 'statement_state_registration_form.html' ,ctx)