# Generated by Django 4.2.4 on 2024-07-01 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_customer_trashed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', ' Male'), ('Female', 'Female'), ('Other', 'Other')], default='', max_length=100),
        ),
    ]
