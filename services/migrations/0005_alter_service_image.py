# Generated by Django 4.0.3 on 2022-03-28 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_service_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]