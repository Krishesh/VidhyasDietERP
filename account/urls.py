from django.contrib.auth.views import LoginView
from django.urls import path
from account import views

app_name = 'account'

urlpatterns = [

    path('account_list', views.account_list, name='account_list'),
]
