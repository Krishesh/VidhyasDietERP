from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def department_list(request):
    return render(request,'humanresource/department/department_list.html')