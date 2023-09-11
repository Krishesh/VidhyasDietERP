from django.contrib import admin

from inquiry.models import Inquiry, Customer_Family_Disease

# Register your models here.
admin.site.register(Customer_Family_Disease)
admin.site.register(Inquiry)
