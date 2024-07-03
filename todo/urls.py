from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('toggle/<int:todo_id>/', views.toggle_completed, name='toggle_completed'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('trash/<int:todo_id>/', views.trash_todo, name='trash_todo'),
]
