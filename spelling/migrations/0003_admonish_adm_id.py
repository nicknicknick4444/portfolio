# Generated by Django 3.2.12 on 2022-03-09 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spelling', '0002_admonish'),
    ]

    operations = [
        migrations.AddField(
            model_name='admonish',
            name='adm_id',
            field=models.IntegerField(default=0),
        ),
    ]
