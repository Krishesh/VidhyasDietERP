# Generated by Django 4.2.4 on 2024-06-29 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_authentication', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Dietitian', 'Dietitian'), ('Therapist', 'Therapist'), ('Guest', 'Guest'), ('', 'default')], default='default', max_length=10),
        ),
    ]
