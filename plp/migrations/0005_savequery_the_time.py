# Generated by Django 3.2.12 on 2022-04-01 19:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('plp', '0004_auto_20220401_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='savequery',
            name='the_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
