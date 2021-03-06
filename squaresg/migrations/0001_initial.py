# Generated by Django 3.2.12 on 2022-02-13 15:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exceppo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exceppy', models.TextField(null=True)),
                ('sessiony', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wardle', models.TextField(null=True)),
                ('sessiony', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Scores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namey', models.CharField(default='', max_length=9)),
                ('score', models.IntegerField(default=0)),
                ('duration', models.CharField(default='blank', max_length=30)),
                ('all_seconds', models.IntegerField(default=0)),
                ('attempts', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Squaresy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('square_text', models.CharField(max_length=200)),
                ('number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Times',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('finish_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('attempts', models.IntegerField(default=0)),
                ('sessiony', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='squaresg.question')),
            ],
        ),
    ]
