# Generated by Django 4.2.4 on 2023-12-12 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inquiry", "0009_inquiry_created_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="inquiry",
            name="customer_prescription_list",
            field=models.CharField(blank=True, default="", max_length=500),
        ),
    ]
