# Generated by Django 4.2.7 on 2023-11-11 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0006_alter_bill_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bill',
            name='fname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bill',
            name='lname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bill',
            name='phone_number1',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='bill',
            name='phone_number2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='bill',
            name='state',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='bill',
            name='street1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bill',
            name='street2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='bill',
            name='zipcode',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
