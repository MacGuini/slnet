# Generated by Django 4.2.7 on 2024-03-17 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_profile_is_staff_profile_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]