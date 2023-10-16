# Generated by Django 4.2.4 on 2023-09-20 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0002_alter_customer_diet_plan"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="diet_plan",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="customer.diet_plan_package",
            ),
        ),
    ]
