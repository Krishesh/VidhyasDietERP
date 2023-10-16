from django.contrib import admin

from customer.models import Diet_Plan_Package, Customer, Customer_Stats

# Register your models here.
admin.site.register(Diet_Plan_Package)
admin.site.register(Customer)
admin.site.register(Customer_Stats)