# Generated by Django 3.2.12 on 2022-02-13 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squaresg', '0002_auto_20220213_1544'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
