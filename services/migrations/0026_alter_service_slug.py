# Generated by Django 4.0.3 on 2023-02-22 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0025_service_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=100, unique=True), max_length=300),
        ),
    ]
