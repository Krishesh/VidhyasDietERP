from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('registration_list/', views.registration_list, name='registration_list'),
    path('registration_print/<int:registration_id>/', views.registration_print, name='registration_print'),
    path('inquiry_to_registration_form/', views.inquiry_to_registration_form, name='inquiry_to_registration_form'),
    path('inquiry_to_registration/', views.inquiry_to_registration, name='inquiry_to_registration'),
    path('trash_registration/', views.trash_registration, name='trash_registration'),
    path('edit_registration_form/', views.edit_registration_form, name='edit_registration_form'),
    path('edit_registration/', views.edit_registration, name='edit_registration'),
    path('registration_to_rebook_form/', views.registration_to_rebook_form, name='registration_to_rebook_form'),
    path('registration_to_rebook/', views.registration_to_rebook, name='registration_to_rebook'),

]
