from django.contrib.auth.views import LoginView
from django.urls import path

from .views import DietPlanAPI, DietPlanDetails, CustomerAPI, CustomerDetails

app_name = 'authentication'

urlpatterns = [

    path('api/diet_plan', DietPlanAPI.as_view(), name='DietPlanAPI'),
    path('api/diet_plan/<int:pk>', DietPlanDetails.as_view(), name='DietPlanDetails'),
    path('api/customer', CustomerAPI.as_view(), name='CustomerAPI'),
    path('api/customer/<int:pk>', CustomerDetails.as_view(), name='CustomerDetails'),
]
