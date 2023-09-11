from django.db import models

from customer.models import Customer


class Customer_Family_Disease(models.Model):
    disease = models.CharField(max_length=500, blank=True, default='')
    relation = models.CharField(max_length=500, blank=True, default='')
    age = models.CharField(max_length=500, blank=True, default='')
    note = models.CharField(max_length=500, blank=True, default='')


# Create your models here.
class Inquiry(models.Model):
    customer_name = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True, default='')

    customer_health_state = models.CharField(max_length=500, blank=True, default='')
    customer_any_prescription = models.CharField(max_length=500, blank=True, default='')
    customer_had_full_body_check_up = models.BooleanField(default=False)
    customer_suffered_any_disease = models.CharField(max_length=500, blank=True, default='')
    customer_smoke_alcohol = models.BooleanField(default=False)

    customer_thought_about_workout = models.CharField(max_length=500, blank=True, default='')
    customer_any_symptoms = models.CharField(max_length=500, blank=True, default='')

    customer_family_disease = models.ManyToManyField(Customer_Family_Disease, default='', blank=True)

    note = models.CharField(max_length=5000, blank=True, default='')

    def __str__(self):
        return self.customer_name.name
