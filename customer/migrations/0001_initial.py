# Generated by Django 4.2.4 on 2023-09-20 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, default="", max_length=500)),
                (
                    "contact_person",
                    models.CharField(blank=True, default="", max_length=500),
                ),
                ("age", models.CharField(blank=True, default="", max_length=100)),
                ("gender", models.CharField(blank=True, default="", max_length=100)),
                (
                    "date_of_birth",
                    models.CharField(blank=True, default="", max_length=100),
                ),
                (
                    "profession",
                    models.CharField(blank=True, default="", max_length=100),
                ),
                ("address", models.CharField(blank=True, default="", max_length=100)),
                ("landmark", models.CharField(blank=True, default="", max_length=100)),
                ("city", models.CharField(blank=True, default="", max_length=100)),
                ("state", models.CharField(blank=True, default="", max_length=100)),
                ("country", models.CharField(blank=True, default="", max_length=100)),
                (
                    "contact_number",
                    models.CharField(blank=True, default="", max_length=500),
                ),
                (
                    "phone_number",
                    models.CharField(blank=True, default="", max_length=500),
                ),
                (
                    "social_number",
                    models.CharField(blank=True, default="", max_length=500),
                ),
                ("email", models.CharField(blank=True, default="", max_length=500)),
                (
                    "annual_income",
                    models.CharField(blank=True, default="", max_length=500),
                ),
                ("website", models.CharField(blank=True, default="", max_length=100)),
                ("note", models.CharField(blank=True, default="", max_length=500)),
                ("tag", models.CharField(blank=True, default="", max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Diet_Plan_Package",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("package_name", models.CharField(max_length=555, unique=True)),
                ("package_cost", models.CharField(max_length=555, unique=True)),
                ("package_service", models.CharField(max_length=555, unique=True)),
                ("package_visibility", models.BooleanField(default=True)),
                ("package_validity", models.BooleanField(default=True)),
                (
                    "package_validity_time",
                    models.CharField(max_length=555, unique=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Customer_Stats",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("weight", models.CharField(blank=True, default="", max_length=100)),
                ("height", models.CharField(blank=True, default="", max_length=100)),
                ("bmi", models.CharField(blank=True, default="", max_length=100)),
                ("whr", models.CharField(blank=True, default="", max_length=100)),
                ("entry_date", models.DateField(auto_now_add=True, null=True)),
                (
                    "customer",
                    models.ForeignKey(
                        blank=True,
                        default="",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="customer.customer",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="customer",
            name="diet_plan",
            field=models.ForeignKey(
                blank=True,
                default="",
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="customer.diet_plan_package",
            ),
        ),
    ]
