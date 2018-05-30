from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.registrator_login),
    path('get-all-register', views.get_all_register , name='get-all-register'),
    path('get-statement/<int:id>', views.get_statement , name='get-statement'),
]