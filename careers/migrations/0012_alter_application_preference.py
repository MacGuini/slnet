# Generated by Django 4.0.3 on 2022-06-07 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0011_rename_phone1_application_home_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='preference',
            field=models.CharField(blank=True, choices=[('mobile', 'Call Mobile'), ('home', 'Call Home'), ('work', 'Call Home'), ('text', 'Text'), ('email', 'Email')], default='call', max_length=11, null=True),
        ),
    ]