from django.urls import path , include
from . import views
urlpatterns = [
    path('', views.all_documents),
    path('statement_state_registration/<int:id>', views.add_statement_state_registration , name = 'statement_state_registration'),
    path('application_for_cancelation/<int:id>', views.add_application_for_cancelation, name = 'application_for_cancelation'),

    path('statement_state_registration/', views.add_statement_state_registration , name = 'statement_state_registration'),
    path('add-address', views.add_address , name = 'add-address'),
]
