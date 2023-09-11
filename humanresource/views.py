from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from humanresource.models import Department, Employee, Salary, Payslip, PlaySlip_Code
from vidhyas_api.serializers import DepartmentSerializer, EmployeeSerializer, SalarySerializer, PayslipSerializer, PlaySlip_CodeSerializer


def department_list(request):
    print(Department.objects.all())
    context = {
        'department': Department.objects.all()
    }
    return render(request, 'humanresource/department/department.html',context )

def employee_list(request):
    print(Employee.objects.all())
    context = {
        'department': Department.objects.all(),
        'employee': Employee.objects.all()
    }
    return render(request, 'humanresource/employee/employee.html',context )

def salary_list(request):
    print(Salary.objects.all())
    context = {
        'salary': Salary.objects.all()
    }
    return render(request, 'humanresource/salary/salary.html',context )

def payslip_list(request):
    print(Payslip.objects.all())
    context = {
        'payslip': Payslip.objects.all()
    }
    return render(request, 'humanresource/payslip/payslip.html',context )

def playSlip_Code_list(request):
    print(PlaySlip_Code.objects.all())
    context = {
        'playSlip_Code': PlaySlip_Code.objects.all()
    }
    return render(request, 'humanresource/playSlip_Code/playSlip_Code.html',context )