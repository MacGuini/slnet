# Generated by Django 4.0.3 on 2022-04-20 23:43

import careers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0006_remove_application_jobs_application_job'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'ordering': ['-created']},
        ),
        migrations.RemoveField(
            model_name='application',
            name='phoneNumber',
        ),
        migrations.RemoveField(
            model_name='application',
            name='secondPhoneNumber',
        ),
        migrations.AddField(
            model_name='application',
            name='area1',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='area2',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='central1',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='central2',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='line1',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='line2',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
