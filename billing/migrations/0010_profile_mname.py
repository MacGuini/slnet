# Generated by Django 4.2.7 on 2023-11-12 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_profile_area1_remove_profile_area2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
