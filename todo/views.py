from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from todo.models import TodoItem


# Create your views here.
def add_todo(request):
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            todo = TodoItem.objects.create(title=title)
            return JsonResponse({'success': True, 'id': todo.id, 'title': todo.title, 'completed': todo.completed})
    return JsonResponse({'success': False})


def toggle_completed(request, todo_id):
    todo = get_object_or_404(TodoItem, id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return JsonResponse({'success': True, 'completed': todo.completed})


def trash_todo(request, todo_id):
    todo = get_object_or_404(TodoItem, id=todo_id)
    todo.trashed = True
    todo.save()
    return JsonResponse({'success': True})
