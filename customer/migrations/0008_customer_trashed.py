# Generated by Django 4.2.4 on 2024-06-29 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_alter_diet_plan_package_package_validity_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='trashed',
            field=models.BooleanField(default=False),
        ),
    ]
