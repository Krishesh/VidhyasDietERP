from django.db import models

from customer.models import Customer


# Create your models here.
class Registration(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True, default='')
    employee = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True, default='')
    account_by = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True, default='')

    trash = models.BooleanField(default=False)

    registration_status = models.CharField(max_length=255, blank=True, default='')

    total_amount = models.CharField(max_length=5000, blank=True, default='')
    received_amount = models.CharField(max_length=5000, blank=True, default='')
    due_amount = models.CharField(max_length=5000, blank=True, default='')
    receipt_bill_no = models.CharField(max_length=5000, blank=True, default='')

    note = models.CharField(max_length=5000, blank=True, default='')

    def __str__(self):
        return self.customer.name
