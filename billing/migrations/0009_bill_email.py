# Generated by Django 4.2.7 on 2023-11-11 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0008_rename_phone_number1_bill_home_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
    ]
