# Generated by Django 4.2.7 on 2023-11-11 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_profile_phone_number1_profile_phone_number2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='phone_number1',
            new_name='home',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='phone_number2',
            new_name='mobile',
        ),
        migrations.AddField(
            model_name='profile',
            name='work',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
