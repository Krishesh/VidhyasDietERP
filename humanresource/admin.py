from django.contrib import admin

from humanresource.models import Department, Employee, Salary, Payslip

# Register your models here.
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Salary)
admin.site.register(Payslip)
