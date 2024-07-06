from django.contrib.auth.views import LoginView
from django.urls import path

from diet.views import (create_logbook_and_stats, body_composition, create_diet_plan_new, create_diet_plan,
                        edit_diet_plan, diet_plan_list,diet_plan_print_nepali,diet_plan_print_english,diet_plan_trash,diet_plan_preview)

app_name = 'diet'

urlpatterns = [
    path('create_logbook_and_stats/', create_logbook_and_stats, name='create_logbook_and_stats'),
    path('create_logbook_and_stats/<int:pk>/', create_logbook_and_stats, name='edit_logbook_and_stats'),

    path('bmi/', body_composition, name='bmi'),
    path('bmi/<int:pk>/', body_composition, name='edit_bmi'),

    # path('diet_plan/', create_or_edit_diet_plan, name='create_diet_plan'),
    # path('diet_plan/<int:pk>/', create_or_edit_diet_plan, name='edit_diet_plan'),

    path('diet_plan_preview/<int:pk>/', diet_plan_preview, name='diet_plan_preview'),
    path('create_diet_plan_new/', create_diet_plan, name='create_diet_plan'),
    path('diet_plan/<int:pk>/edit/', edit_diet_plan, name='edit_diet_plan'),
    path('diet_plan/new/<int:customer_id_pk>/', create_diet_plan_new, name='create_diet_plan_new'),
    path('diet_plan_list/', diet_plan_list, name='diet_plan_list'),
    path('diet_plan_print_nepali/<int:pk>/', diet_plan_print_nepali, name='diet_plan_print_nepali'),
    path('diet_plan_print_english/<int:pk>/', diet_plan_print_english, name='diet_plan_print_english'),
    path('diet_plan_trash/', diet_plan_trash, name='diet_plan_trash'),

]
