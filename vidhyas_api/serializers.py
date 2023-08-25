from rest_framework import serializers
from humanresource.models import Department, Employee, Salary, Payslip, PlaySlip_Code
from humanresource.models import Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'


class PayslipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payslip
        fields = '__all__'


class PlaySlip_CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaySlip_Code
        fields = '__all__'
