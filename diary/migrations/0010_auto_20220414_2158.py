# Generated by Django 3.2.12 on 2022-04-14 20:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0009_rename_date_modified_entry_last_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='created',
            field=models.DateField(default=datetime.datetime(2022, 4, 14, 20, 58, 17, 404677, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entry',
            name='last_modified',
            field=models.DateField(),
        ),
    ]
