# Generated by Django 3.2.12 on 2022-04-01 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=200)),
                ('q_res', models.CharField(max_length=5000)),
            ],
        ),
        migrations.DeleteModel(
            name='SaveImage',
        ),
    ]
