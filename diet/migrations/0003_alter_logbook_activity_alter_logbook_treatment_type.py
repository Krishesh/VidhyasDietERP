# Generated by Django 4.2.4 on 2024-07-02 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0002_logbook_after_weight_logbook_before_weight_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logbook',
            name='activity',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='logbook',
            name='treatment_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
