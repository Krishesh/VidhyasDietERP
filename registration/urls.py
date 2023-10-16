from django.urls import path
from . import views

app_name = 'inquiry'

urlpatterns = [
    path('registration_list/', views.registration_list, name='registration_list'),

]
