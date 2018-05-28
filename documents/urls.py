from django.urls import path , include
from . import views
urlpatterns = [
    path('', views.all_documents),
    path('statement_state_registration/<int:id>', views.add_statement_state_registration , name = 'statement_state_registration'),

]
