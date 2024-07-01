from django.urls import path
from . import views

app_name = 'humanresource'

urlpatterns = [
    path('department/', views.department_list, name='department_list'),
    path('department/<int:pk>/', views.department_list, name='edit_department'),
    path('delete_department/', views.delete_department, name='delete_department'),

    path('employee/', views.employee_list, name='employee_list'),
    path('employee_details/', views.employee_details, name='employee_details'),
    path('add_employee_form/', views.add_employee_form, name='add_employee_form'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('edit_employee_form/', views.edit_employee_form, name='edit_employee_form'),
    path('edit_employee/', views.edit_employee, name='edit_employee'),
    path('delete_employee/', views.delete_employee, name='delete_employee'),

]
