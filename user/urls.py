from django.urls import path , include
from . import views
urlpatterns = [
    path('', views.test),
    path('login', views.login , name = 'login'),
    path('register', views.register , name='register'),
    path('personal-info/<int:id>', views.personal_info , name='personal-info'),
    path('contact-data/<int:id>', views.contact_data, name='contact-data'),
    path('update-contact/<int:id>', views.update_contact, name='update-contact'),
    path('menu/<int:id>', views.menu, name='menu'),
    path('get-info-dovidky/<int:id>', views.get_info_dovidky, name='get-info-dovidky'),
    path('change-password/<int:id>', views.change_password, name='change-password'),
    path('logout/', views.logout, name='logout'),
    path('previous/', views.previous, name='previous'),
    path('search-for-adress/', views.search_for_adress, name='search-for-adress'),
    path('get-info', views.get_info, name='get-info'),
]
