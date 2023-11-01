from django.db import models

from customer.models import Customer


class Customer_Family_Disease(models.Model):
    disease = models.CharField(max_length=500, blank=True, default='')
    relation = models.CharField(max_length=500, blank=True, default='')
    age = models.CharField(max_length=500, blank=True, default='')
    note = models.CharField(max_length=500, blank=True, default='')

    def __str__(self):
        return self.disease


# Create your models here.
class Inquiry(models.Model):
    inquiry_id = models.CharField(max_length=255, blank=True, default='')
    created_date = models.DateTimeField(null=True, blank=True)

    customer_name = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True, default='')

    trash = models.BooleanField(default=False)
    inquiry_status = models.CharField(max_length=255, blank=True, default='')
    inquiry_source = models.CharField(max_length=255, blank=True, default='')

    customer_health_state = models.CharField(max_length=500, blank=True, default='')
    customer_any_prescription = models.CharField(max_length=500, blank=True, default='')
    customer_had_full_body_check_up = models.CharField(max_length=500, blank=True, default='')
    customer_suffered_any_disease = models.CharField(max_length=500, blank=True, default='')

    customer_smoke_alcohol = models.CharField(max_length=500, blank=True, default='')

    customer_thought_about_workout = models.CharField(max_length=500, blank=True, default='')
    customer_activity_level = models.CharField(max_length=500, blank=True, default='')

    customer_any_symptoms = models.CharField(max_length=500, blank=True, default='')
    customer_lifestyle = models.CharField(max_length=500, blank=True, null=True, default='')

    customer_family_disease = models.ManyToManyField(Customer_Family_Disease, default='', blank=True)

    note = models.CharField(max_length=5000, blank=True, default='')

    def __str__(self):
        return self.customer_name.name
