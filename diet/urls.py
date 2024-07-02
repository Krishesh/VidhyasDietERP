from django.contrib.auth.views import LoginView
from django.urls import path

from diet.views import create_logbook_and_stats,body_composition

app_name = 'diet'

urlpatterns = [
    path('create_logbook_and_stats/', create_logbook_and_stats, name='create_logbook_and_stats'),
    path('create_logbook_and_stats/<int:pk>/', create_logbook_and_stats, name='edit_logbook_and_stats'),

    path('bmi/', body_composition, name='bmi'),
    path('bmi/<int:pk>/', body_composition, name='edit_bmi'),
]
