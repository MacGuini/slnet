# Generated by Django 4.0.3 on 2022-09-09 17:37

import careers.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0021_application_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes/', validators=[careers.validators.validate_file_size]),
        ),
    ]
