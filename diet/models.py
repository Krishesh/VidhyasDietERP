from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models

from customer.models import Customer, Customer_Stats


# Body Composition model
class BodyComposition(models.Model):
    weight = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    muscle_mass = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fat_percentage = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bone_density = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bmr = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bmi = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    body_water = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    protein = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_intake_calories = models.DecimalField(max_digits=10, decimal_places=2, default=0)

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


class DietPlan(models.Model):
    trashed = models.BooleanField(default=False)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
                                   related_name="diet_plan_created_by")
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='approved_by')
    created_date = models.DateField(auto_now_add=True)

    days = (('Everyday', 'Everyday'),
            ('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'),
            ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'))
    day = models.CharField(max_length=100, choices=days, default='EveryDay')

    cereals_pulses = models.CharField(max_length=100, default='1')
    vegetables = models.CharField(max_length=100, default='1')
    fruits = models.CharField(max_length=100, default='1')
    meat_eggs = models.CharField(max_length=100, default='1')
    milk_products = models.CharField(max_length=100, default='1')
    fat_oil_products = models.CharField(max_length=100, default='1')

    breakfast_time = models.CharField(max_length=100, default='6:30 AM')
    breakfast_select = (
        ('Wheat', 'Wheat'), ('Maize', 'Maize'), ('Buckwheat', 'Buckwheat'), ('Finger Millet', 'Finger Millet'),)
    breakfast_chapatti_select = models.CharField(max_length=100, choices=breakfast_select, default='Wheat')
    breakfast_chapatti = models.CharField(max_length=100, default='1')
    breakfast_dry_bread = models.CharField(max_length=100, default='1')
    breakfast_oats_cereals = models.CharField(max_length=100, default='1')
    breakfast_egg = models.CharField(max_length=100, default='1')
    breakfast_vegetables = models.CharField(max_length=100, default='1')

    mid_morning_snack_time = models.CharField(max_length=100, default='9:30 AM')
    mid_morning_fruits = models.CharField(max_length=100, default='1')
    mid_morning_yogurt_select = models.CharField(max_length=100,
                                                 choices=(('Yogurt/Curd', 'Yogurt/Curd'), ('Buttermilk', 'Buttermilk')),
                                                 default='yogurt')
    mid_morning_yogurt = models.CharField(max_length=100, default='1')

    lunch_time = models.CharField(max_length=100, default='12:30 PM')
    rice_select = (('Rice', 'Rice'), ('Dhindo', 'Dhindo'), ('Chakla', 'Chakla'))
    lunch_rice_select = models.CharField(max_length=100, choices=rice_select, default='rice')
    lunch_rice = models.CharField(max_length=100, default='1')
    lunch_roti = models.CharField(max_length=100, default='1')
    lunch_lentils = models.CharField(max_length=100, default='1')
    lunch_vegetable_curry = models.CharField(max_length=100, default='1')
    lunch_leafy_vegetables = models.CharField(max_length=100, default='1')
    lunch_meat_select = models.CharField(max_length=100,
                                         choices=(('Meat', 'Meat'), ('Tofu', 'Tofu'), ('Paneer', 'Paneer')),
                                         default='meat')
    lunch_meat_tofu = models.CharField(max_length=100, default='1')
    lunch_fish = models.CharField(max_length=100, default='1')

    afternoon_snack_time = models.CharField(max_length=100, default='4:30 PM')
    afternoon_snack_sandwich = models.CharField(max_length=100, default='1')
    afternoon_snack_bread_roll = models.CharField(max_length=100, default='1')
    afternoon_snack_beaten_rice = models.CharField(max_length=100, default='1')
    afternoon_snack_roasted_corn = models.CharField(max_length=100, default='1')
    afternoon_snack_pulses = models.CharField(max_length=100, default='1')
    afternoon_snack_raw_vegetables = models.CharField(max_length=100, default='1')

    dinner_time = models.CharField(max_length=100, default='8:30 AM')
    dinner_rice_dhindo_select = models.CharField(max_length=100, choices=rice_select, default='rice')
    dinner_rice_dhindo = models.CharField(max_length=100, default='1')
    dinner_dry_bread = models.CharField(max_length=100, default='1')
    dinner_lentils = models.CharField(max_length=100, default='1')
    dinner_vegetables = models.CharField(max_length=100, default='1')

    carbohydrates_calories = models.CharField(max_length=100, default='1')
    carbohydrates_grams = models.CharField(max_length=100, default='1')
    proteins_calories = models.CharField(max_length=100, default='1')
    proteins_grams = models.CharField(max_length=100, default='1')
    fat_calories = models.CharField(max_length=100, default='1')
    fat_grams = models.CharField(max_length=100, default='1')
    total_calories = models.CharField(max_length=100, default='1')

    activity_level = models.CharField(max_length=100, default='1')

    remarks = models.TextField(blank=True, null=True)
    follow_up_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'Diet Plan for {self.customer.name}'
