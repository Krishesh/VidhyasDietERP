# Generated by Django 4.2.4 on 2024-07-02 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logbook',
            name='after_weight',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='logbook',
            name='before_weight',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='logbook',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]