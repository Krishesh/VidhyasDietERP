from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models

from customer.models import Customer, Customer_Stats


# Body Composition model
class BodyComposition(models.Model):
    weight = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    muscle_mass = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    fat_percentage = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    bone_density = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    bmr = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    bmi = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    body_water = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    recorded_at = models.DateTimeField(auto_now_add=True)

    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def create_customer_stats(self):
        # Create a new Customer_Stats entry
        new_stats = Customer_Stats(
            customer=self.client,
            entry_date=self.recorded_at,
        )

        # Set the weight value based on LogBook
        if self.weight:
            new_stats.weight = self.weight
        else:
            new_stats.weight = 0.0
        if self.bmi:
            new_stats.bmi = self.bmi
        else:
            new_stats.bmi = 0.0

        # Set other fields as needed, ensure default values for missing data
        new_stats.whr = new_stats.whr if new_stats.whr else 0.0
        new_stats.remark = new_stats.whr if new_stats.whr else 'BodyComposition'

        new_stats.save()


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
    before_weight = models.CharField(max_length=100, null=True, blank=True, default='')
    after_weight = models.CharField(max_length=100, null=True, blank=True, default='')
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    activity = models.TextField(null=True, blank=True)
    treatment_type = models.CharField(max_length=100, null=True, blank=True)

    trashed = models.BooleanField(default=False)

    def create_or_update_customer_stats(self):
        # Create a new Customer_Stats entry
        new_stats = Customer_Stats(
            customer=self.client,
            entry_date=self.date,
        )

        # Set the weight value based on LogBook
        if self.before_weight:
            new_stats.weight = self.before_weight
        elif self.after_weight:
            new_stats.weight = self.after_weight

        # Set other fields as needed, ensure default values for missing data
        new_stats.bmi = new_stats.bmi if new_stats.bmi else 0.0
        new_stats.whr = new_stats.whr if new_stats.whr else 0.0
        new_stats.remark = new_stats.whr if new_stats.whr else 'LogBook'

        new_stats.save()

    def __str__(self):
        return f"LogBook entry for {self.client.name} by {self.create_by.username} on {self.date}"


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
