# Generated by Django 4.2.4 on 2024-07-04 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0007_alter_bodycomposition_bmi_alter_bodycomposition_bmr_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bodycomposition',
            name='protein',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='bodycomposition',
            name='total_intake_calories',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]