from django.db import models

from customer.models import Customer
from humanresource.models import Employee
from inquiry.models import Inquiry


# Create your models here.
class Registration(models.Model):

    registration_id = models.CharField(max_length=255, blank=True, default='')
    registration_date = models.DateTimeField(null=True, blank=True)

    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True, default='',related_name="customer",db_constraint=False)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, blank=True, default='',related_name="employee",db_constraint=False)
    account_by = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, blank=True, default='',related_name="account_by",db_constraint=False)
    inquiry = models.ForeignKey(Inquiry, on_delete=models.DO_NOTHING, blank=True, default='',related_name="inquiry",db_constraint=False)

    trash = models.BooleanField(default=False)

    registration_status = models.CharField(max_length=255, blank=True, default='')

    discount_amount = models.CharField(max_length=5000, blank=True, default='')
    total_amount = models.CharField(max_length=5000, blank=True, default='')
    received_amount = models.CharField(max_length=5000, blank=True, default='')
    due_amount = models.CharField(max_length=5000, blank=True, default='')
    receipt_bill_no = models.CharField(max_length=5000, blank=True, default='')

    package_booked = models.CharField(max_length=5000, blank=True, default='')
    package_cost = models.CharField(max_length=5000, blank=True, default='')
    package_service = models.CharField(max_length=5000, blank=True, default='')
    therapy_package_start = models.DateField(null=True, blank=True)
    therapy_package_end = models.DateField(null=True, blank=True)
    gym_package_start = models.DateField(null=True, blank=True)
    gym_package_end = models.DateField(null=True, blank=True)

    note = models.CharField(max_length=5000, blank=True, default='')

    def __str__(self):
        return self.customer.name
