# Generated by Django 4.0.3 on 2023-02-04 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0023_portfolio_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
