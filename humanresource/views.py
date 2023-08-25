from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from humanresource.models import Department
from vidhyas_api.serializers import DepartmentSerializer

from humanresource.models import Employee
from vidhyas_api.serializers import EmployeeSerializer

def department_list(request):
    print(Department.objects.all())
    context = {
        'department': Department.objects.all()
    }
    return render(request, 'humanresource/department/department.html',context )

def employee_list(request):
    print(Employee.objects.all())
    context = {
        'employee': Employee.objects.all()
    }
    return render(request, 'humanresource/employee/employee.html',context )

