# Generated by Django 4.1 on 2022-08-24 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_event_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='test',
        ),
    ]
