# Generated by Django 4.1 on 2022-08-24 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_event_description_event_paragraph'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='test',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
