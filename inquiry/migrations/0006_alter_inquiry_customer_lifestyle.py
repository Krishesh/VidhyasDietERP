# Generated by Django 4.2.4 on 2023-09-23 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inquiry", "0005_inquiry_trash"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inquiry",
            name="customer_lifestyle",
            field=models.CharField(blank=True, default="", max_length=500, null=True),
        ),
    ]