# Generated by Django 4.0.3 on 2023-02-22 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0024_alter_service_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', max_length=300),
        ),
    ]