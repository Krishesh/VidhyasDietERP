# Generated by Django 4.2.4 on 2025-05-22 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0014_dietplan_follow_up_date_alter_dietplan_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodycomposition',
            name='bmi',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='bodycomposition',
            name='bmr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='bodycomposition',
            name='body_water',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='bodycomposition',
            name='bone_density',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='bodycomposition',
            name='fat_percentage',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='bodycomposition',
            name='muscle_mass',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='bodycomposition',
            name='protein',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='bodycomposition',
            name='total_intake_calories',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='bodycomposition',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
