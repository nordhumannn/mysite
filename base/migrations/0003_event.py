# Generated by Django 4.1 on 2022-08-23 11:51

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_dish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('is_visible', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to=base.models.Event.get_file_name)),
            ],
        ),
    ]