# Generated by Django 4.2.7 on 2023-11-11 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0007_bill_city_bill_fname_bill_lname_bill_phone_number1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='phone_number1',
            new_name='home',
        ),
        migrations.RenameField(
            model_name='bill',
            old_name='phone_number2',
            new_name='mobile',
        ),
        migrations.AddField(
            model_name='bill',
            name='work',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]