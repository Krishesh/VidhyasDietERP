from django.contrib.auth.models import User
from django.db import models

from customer.models import Customer
from humanresource.models import Employee


# Create your models here.
class Account(models.Model):
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    account_created_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='account_created_by')

    billing_status = models.CharField(max_length=20, choices=[('Paid', 'Paid'), ('Due', 'Due')])
    monthly_paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    total_amount = models.CharField(max_length=500, blank=True, default='')
    received_amount = models.CharField(max_length=500, blank=True, default='')
    due_amount = models.CharField(max_length=500, blank=True, default='')
    receipt_bill_no = models.CharField(max_length=500, blank=True, default='')

    account_reference = models.CharField(max_length=500, blank=True, default='')
    entry_date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.client.name
