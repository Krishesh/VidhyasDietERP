# Generated by Django 4.2.4 on 2024-07-02 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0003_alter_logbook_activity_alter_logbook_treatment_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='logbook',
            name='trashed',
            field=models.BooleanField(default=False),
        ),
    ]