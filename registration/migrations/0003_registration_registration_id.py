# Generated by Django 4.2.4 on 2023-10-27 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0002_registration_inquiry"),
    ]

    operations = [
        migrations.AddField(
            model_name="registration",
            name="registration_id",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
    ]