# Generated by Django 3.2.12 on 2022-04-10 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0005_auto_20220410_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date_for',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='entry',
            name='date_written',
            field=models.DateField(),
        ),
    ]
