from django.contrib import admin

from humanresource.models import Department, Employee, Salary, Payslip, PlaySlip_Code

# Register your models here.
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Salary)
admin.site.register(Payslip)
admin.site.register(PlaySlip_Code)
