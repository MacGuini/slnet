# Generated by Django 4.0.3 on 2022-09-10 20:42

import careers.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0022_alter_application_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes/', validators=[careers.validators.validate_file_size, django.core.validators.FileExtensionValidator(allowed_extensions=['xml'])]),
        ),
    ]
