# Generated by Django 4.0.3 on 2022-04-04 03:37

import careers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0004_alter_application_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='phoneNumber',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='secondPhoneNumber',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]