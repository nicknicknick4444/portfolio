# Generated by Django 3.2.12 on 2022-03-09 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spelling', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admonish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adm_text', models.CharField(default='', max_length=280)),
            ],
        ),
    ]
