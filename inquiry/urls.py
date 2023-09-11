from django.urls import path
from . import views

app_name = 'inquiry'

urlpatterns = [
    path('inquiry_list/', views.inquiry_list, name='inquiry_list'),
    path('add_inquiry/', views.add_inquiry, name='add_inquiry'),

]
