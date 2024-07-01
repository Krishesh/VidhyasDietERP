from django.contrib.auth.views import LoginView
from django.urls import path

from customer.views import (DietPlanAPI, DietPlanDetails, CustomerAPI, CustomerDetails, customer_list, add_customer,
                            edit_customer, trash_customer, customer_detail)

app_name = 'customer'

urlpatterns = [

    path('api/diet_plan', DietPlanAPI.as_view(), name='DietPlanAPI'),
    path('api/diet_plan/<int:pk>', DietPlanDetails.as_view(), name='DietPlanDetailsApi'),
    path('api/customer', CustomerAPI.as_view(), name='CustomerAPI'),
    path('api/customer/<int:pk>', CustomerDetails.as_view(), name='CustomerDetailsApi'),

    path('customer/<int:pk>/', customer_detail, name='customer_detail'),
    path('customer_list/', customer_list, name='customer_list'),
    path('add_customer/', add_customer, name='add_customer'),
    path('edit_customer/<int:pk>/', edit_customer, name='edit_customer'),
    path('trash_customer/', trash_customer, name='trash_customer'),
]
