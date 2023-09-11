from django.urls import path
from . import views

app_name = 'humanresource'

urlpatterns = [
    path('department/', views.department_list, name='department_list'),

]
