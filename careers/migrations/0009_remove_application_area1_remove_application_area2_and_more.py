# Generated by Django 4.0.3 on 2022-06-07 15:03

import careers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0008_alter_application_zipcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='area1',
        ),
        migrations.RemoveField(
            model_name='application',
            name='area2',
        ),
        migrations.RemoveField(
            model_name='application',
            name='central1',
        ),
        migrations.RemoveField(
            model_name='application',
            name='central2',
        ),
        migrations.RemoveField(
            model_name='application',
            name='line1',
        ),
        migrations.RemoveField(
            model_name='application',
            name='line2',
        ),
        migrations.AddField(
            model_name='application',
            name='home_num',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='mobile_num',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
