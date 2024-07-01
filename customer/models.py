from django.db import models
choose_gender = (
    ('Male', ' Male'), ('Female', 'Female'), ('Other', 'Other')
)
# Create your models here.

# Create your models here.
class Diet_Plan_Package(models.Model):
    package_name = models.CharField(max_length=555, unique=True)
    package_cost = models.CharField(max_length=555, unique=True)
    package_service = models.CharField(max_length=555, unique=True)

    package_visibility = models.BooleanField(default=True)
    package_validity = models.BooleanField(default=True)

    package_validity_time = models.CharField(max_length=555)

    # package_validity_time_start = models.DateField(null=True, blank=True)
    # package_validity_time_end = models.DateField(null=True, blank=True)
    # therapy_package_validity_time_start = models.DateField(null=True, blank=True)
    # therapy_package_validity_time_end =  models.DateField(null=True, blank=True)
    # gym_package_validity_time_start =  models.DateField(null=True, blank=True)
    # gym_package_validity_time_end = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.package_name


class Customer(models.Model):
    name = models.CharField(max_length=500, blank=True, default='')
    contact_person = models.CharField(max_length=500, blank=True, default='')

    age = models.CharField(max_length=100, blank=True, default='')
    gender = models.CharField(max_length=100,choices=choose_gender, blank=True, default='')
    date_of_birth = models.CharField(max_length=100, blank=True, default='')
    profession = models.CharField(max_length=100, blank=True, default='')

    address = models.CharField(max_length=100, blank=True, default='')
    landmark = models.CharField(max_length=100, blank=True, default='')
    city = models.CharField(max_length=100, blank=True, default='')
    state = models.CharField(max_length=100, blank=True, default='')
    country = models.CharField(max_length=100, blank=True, default='')

    contact_number = models.CharField(max_length=500, blank=True, default='')
    phone_number = models.CharField(max_length=500, blank=True, default='')
    social_number = models.CharField(max_length=500, blank=True, default='')
    email = models.CharField(max_length=500, blank=True, default='')

    annual_income = models.CharField(max_length=500, blank=True, default='')

    website = models.CharField(max_length=100, blank=True, default='')
    note = models.CharField(max_length=500, blank=True, default='')

    diet_plan = models.ForeignKey(Diet_Plan_Package, on_delete=models.DO_NOTHING, null=True, blank=True)

    # for clients
    tag = models.CharField(max_length=100, blank=True, default='')

    trashed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Customer_Stats(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=True, default='')
    weight = models.CharField(max_length=100, null=True, blank=True, default='')
    height = models.CharField(max_length=100, null=True, blank=True, default='')
    waist = models.CharField(max_length=100, null=True, blank=True, default='')
    hip = models.CharField(max_length=100, null=True, blank=True, default='')
    bmi = models.FloatField(max_length=100, null=True, blank=True, default='')
    whr = models.FloatField(max_length=100, null=True, blank=True, default='')
    entry_date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.customer.name
