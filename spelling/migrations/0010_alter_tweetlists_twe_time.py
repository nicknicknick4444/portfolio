# Generated by Django 3.2.12 on 2022-03-12 10:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('spelling', '0009_alter_tweetlists_twe_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweetlists',
            name='twe_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 12, 10, 16, 17, 220957, tzinfo=utc)),
        ),
    ]