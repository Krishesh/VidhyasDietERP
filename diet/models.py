from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models

from customer.models import Customer


# Body Composition model
class BodyComposition(models.Model):
    muscle_mass = models.DecimalField(max_digits=5, decimal_places=2)
    fat_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    bone_density = models.DecimalField(max_digits=5, decimal_places=2)
    bmr = models.DecimalField(max_digits=5, decimal_places=2)
    bmi = models.DecimalField(max_digits=5, decimal_places=2)
    body_water = models.DecimalField(max_digits=5, decimal_places=2)
    recorded_at = models.DateTimeField(auto_now_add=True)

    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)


# Diet Chart model
class DietChart(models.Model):
    dietitian = models.ForeignKey(User, related_name='dietitian', on_delete=models.CASCADE)
    diet_plan = models.TextField()
    verification_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)


# Log Book model
class LogBook(models.Model):
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)

    date = models.DateField()
    activity = models.TextField()
    treatment_type = models.CharField(max_length=100)


# Package Schedule model
class PackageSchedule(models.Model):
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)

    package_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    treatment_details = models.TextField()


# Graph model (if needed to store graph-related data)
class Graph(models.Model):
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)

    graph_type = models.CharField(max_length=100)
    graph_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
