# Generated by Django 4.2.4 on 2023-10-28 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0006_alter_customer_stats_bmi_alter_customer_stats_whr"),
    ]

    operations = [
        migrations.AlterField(
            model_name="diet_plan_package",
            name="package_validity_time",
            field=models.CharField(max_length=555),
        ),
    ]
