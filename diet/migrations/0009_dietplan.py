# Generated by Django 4.2.4 on 2024-07-06 07:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_alter_customer_stats_entry_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diet', '0008_bodycomposition_protein_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DietPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('day', models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Everyday', 'Everyday')], default='EveryDay', max_length=100)),
                ('cereals_pulses', models.CharField(default='1', max_length=100)),
                ('vegetables', models.CharField(default='1', max_length=100)),
                ('fruits', models.CharField(default='1', max_length=100)),
                ('meat_eggs', models.CharField(default='1', max_length=100)),
                ('milk_products', models.CharField(default='1', max_length=100)),
                ('fat_oil_products', models.CharField(default='1', max_length=100)),
                ('breakfast_time', models.CharField(default='6:30 AM', max_length=100)),
                ('breakfast_chapatti_select', models.CharField(choices=[('Wheat', 'Wheat'), ('Maize', 'Maize'), ('Buckwheat', 'Buckwheat'), ('Finger Millet', 'Finger Millet')], default='Wheat', max_length=100)),
                ('breakfast_chapatti', models.CharField(default='1', max_length=100)),
                ('breakfast_dry_bread', models.CharField(default='1', max_length=100)),
                ('breakfast_oats_cereals', models.CharField(default='1', max_length=100)),
                ('breakfast_egg', models.CharField(default='1', max_length=100)),
                ('breakfast_vegetables', models.CharField(default='1', max_length=100)),
                ('mid_morning_snack_time', models.CharField(default='9:30 AM', max_length=100)),
                ('mid_morning_fruits', models.CharField(default='1', max_length=100)),
                ('mid_morning_yogurt_select', models.CharField(choices=[('Yogurt/Curd', 'Yogurt/Curd'), ('Buttermilk', 'Buttermilk')], default='yogurt', max_length=100)),
                ('mid_morning_yogurt', models.CharField(default='1', max_length=100)),
                ('lunch_time', models.CharField(default='6:30 AM', max_length=100)),
                ('lunch_rice_select', models.CharField(choices=[('Rice', 'Rice'), ('Dhindo', 'Dhindo'), ('Chakla', 'Chakla')], default='rice', max_length=100)),
                ('lunch_rice', models.CharField(default='1', max_length=100)),
                ('lunch_roti', models.CharField(default='1', max_length=100)),
                ('lunch_lentils', models.CharField(default='1', max_length=100)),
                ('lunch_vegetable_curry', models.CharField(default='1', max_length=100)),
                ('lunch_leafy_vegetables', models.CharField(default='1', max_length=100)),
                ('lunch_meat_select', models.CharField(choices=[('Meat', 'Meat'), ('Tofu', 'Tofu'), ('Paneer', 'Paneer')], default='meat', max_length=100)),
                ('lunch_meat_tofu', models.CharField(default='1', max_length=100)),
                ('lunch_fish', models.CharField(default='1', max_length=100)),
                ('afternoon_snack_time', models.CharField(default='6:30 AM', max_length=100)),
                ('afternoon_snack_sandwich', models.CharField(default='1', max_length=100)),
                ('afternoon_snack_bread_roll', models.CharField(default='1', max_length=100)),
                ('afternoon_snack_beaten_rice', models.CharField(default='1', max_length=100)),
                ('afternoon_snack_roasted_corn', models.CharField(default='1', max_length=100)),
                ('afternoon_snack_pulses', models.CharField(default='1', max_length=100)),
                ('afternoon_snack_raw_vegetables', models.CharField(default='1', max_length=100)),
                ('dinner_time', models.CharField(default='6:30 AM', max_length=100)),
                ('dinner_rice_dhindo', models.CharField(choices=[('Rice', 'Rice'), ('Dhindo', 'Dhindo'), ('Chakla', 'Chakla')], default='1', max_length=100)),
                ('dinner_dry_bread', models.CharField(default='1', max_length=100)),
                ('dinner_lentils', models.CharField(default='1', max_length=100)),
                ('dinner_vegetables', models.CharField(default='1', max_length=100)),
                ('carbohydrates_calories', models.CharField(default='1', max_length=100)),
                ('carbohydrates_grams', models.CharField(default='1', max_length=100)),
                ('proteins_calories', models.CharField(default='1', max_length=100)),
                ('proteins_grams', models.CharField(default='1', max_length=100)),
                ('fat_calories', models.CharField(default='1', max_length=100)),
                ('fat_grams', models.CharField(default='1', max_length=100)),
                ('total_calories', models.CharField(default='1', max_length=100)),
                ('activity_level', models.CharField(default='1', max_length=100)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
    ]