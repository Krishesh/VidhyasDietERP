# Generated by Django 4.2.4 on 2023-09-20 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inquiry", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inquiry",
            name="customer_smoke_alcohol",
            field=models.CharField(blank=True, default="", max_length=500),
        ),
    ]