# Generated by Django 3.2.12 on 2022-02-17 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squaresg', '0004_clab'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clab',
            new_name='FirstInd',
        ),
        migrations.RenameField(
            model_name='firstind',
            old_name='clab',
            new_name='first_ind',
        ),
    ]
