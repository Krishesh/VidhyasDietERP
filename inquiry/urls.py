from django.urls import path
from inquiry import views

app_name = 'inquiry'

urlpatterns = [
    path('inquiry_list/', views.inquiry_list, name='inquiry_list'),
    path('add_inquiry_form/', views.add_inquiry_form, name='add_inquiry_form'),
    path('add_inquiry/', views.add_inquiry, name='add_inquiry'),
    path('edit_inquiry_form/', views.edit_inquiry_form, name='edit_inquiry_form'),
    path('edit_inquiry/', views.edit_inquiry, name='edit_inquiry'),
    path('trash_inquiry/', views.trash_inquiry, name='trash_inquiry'),
    path('details_inquiry/', views.details_inquiry, name='details_inquiry'),

]
