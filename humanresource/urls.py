from django.urls import path
from .views import department_api
from django.views.generic.base import TemplateView  # Import TemplateView


app_name = 'humanresource'

urlpatterns = {
    path('api/departments/', department_api.as_view(), name='department_api'),  # Use 'department_api' as the name
    path('department/', TemplateView.as_view(template_name='department/department.html'), name='department_template'),
    # Use TemplateView directly
}