from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from humanresource.models import Department


def department_list(request):
    print(Department.objects.all())
    context = {
        'department': Department.objects.all()
    }
    return render(request, 'humanresource/department/department.html',context )