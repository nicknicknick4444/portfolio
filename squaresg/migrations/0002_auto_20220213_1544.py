# Generated by Django 3.2.12 on 2022-02-13 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squaresg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exceppo',
            name='sessiony',
            field=models.CharField(default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='number',
            name='sessiony',
            field=models.CharField(default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='times',
            name='sessiony',
            field=models.CharField(default='', max_length=1000, null=True),
        ),
    ]
