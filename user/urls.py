from django.urls import path , include
from . import views
urlpatterns = [
    path('', views.test),
    path('login', views.login , name = 'login'),
    path('register', views.register , name='register'),
    path('personal-info/<int:id>', views.personal_info , name='personal-info'),
    path('contact-data/<int:id>', views.contact_data, name='contact-data'),
    path('update-email/<int:id>', views.update_email, name='update-email'),
]
