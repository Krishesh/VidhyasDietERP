# Generated by Django 4.2.4 on 2024-07-06 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0011_alter_customer_stats_entry_date'),
        ('diet', '0011_alter_dietplan_afternoon_snack_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietplan',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='dietplan',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
    ]
