# Generated by Django 3.1.5 on 2021-02-21 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appoinment', '0004_auto_20210219_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Booked', 'Booked')], max_length=200, null=True),
        ),
    ]