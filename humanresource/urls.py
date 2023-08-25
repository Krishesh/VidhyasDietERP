from django.urls import path
from django.views.generic.base import TemplateView  # Import TemplateView
from . import views

app_name = 'humanresource'

urlpatterns = [
    path('department/', views.department_list, name='department_list'),
    path('employee/', views.employee_list, name='employee_list'),
    path('salary/', views.salary_list, name='salary_list'),
    path('playSlip_Code/', views.playSlip_Code_list, name='playSlip_Code_list'),
    path('payslip/', views.payslip_list, name='payslip_list'),
]