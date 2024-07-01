from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

app_name = 'user_authentication'

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout_link/', views.logout_link, name='logout_link'),


]
