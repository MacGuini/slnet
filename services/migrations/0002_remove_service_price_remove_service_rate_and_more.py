# Generated by Django 4.0.3 on 2022-03-26 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='price',
        ),
        migrations.RemoveField(
            model_name='service',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='service',
            name='rate_type',
        ),
    ]