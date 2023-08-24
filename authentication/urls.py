from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('api/login/', LoginView.as_view(), name='login'),


]
