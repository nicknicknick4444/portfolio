# Generated by Django 3.2.12 on 2022-03-11 21:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('spelling', '0006_tweetlists_twe_term'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetlists',
            name='twe_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 11, 21, 44, 47, 9801, tzinfo=utc)),
        ),
    ]
