# Generated by Django 3.2.12 on 2022-04-17 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0011_alter_entry_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='user',
            field=models.CharField(choices=[('a', 'Yes'), ('b', 'No'), ('c', 'maybe')], max_length=5),
        ),
    ]
