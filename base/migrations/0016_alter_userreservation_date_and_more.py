# Generated by Django 4.1 on 2022-08-29 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_userreservation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreservation',
            name='date',
            field=models.DateField(default='29.08.2022'),
        ),
        migrations.AlterField(
            model_name='userreservation',
            name='time',
            field=models.TimeField(default='17:20'),
        ),
    ]
