from django.urls import path
from django.views.generic.base import TemplateView  # Import TemplateView
from . import views

app_name = 'humanresource'

urlpatterns = {
    path('department/', views.department_list, name='department_list'),
    path('employee/', views.employee_list, name='employee_list'),
    # Use TemplateView directly
}