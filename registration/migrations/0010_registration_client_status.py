# Generated by Django 4.2.4 on 2023-12-10 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0009_registration_discount_amount"),
    ]

    operations = [
        migrations.AddField(
            model_name="registration",
            name="client_status",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
    ]
