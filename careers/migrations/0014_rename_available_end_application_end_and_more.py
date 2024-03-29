# Generated by Django 4.0.3 on 2022-06-08 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0013_alter_application_preference'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='available_end',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='available_start',
            new_name='start',
        ),
        migrations.AlterField(
            model_name='application',
            name='preference',
            field=models.CharField(choices=[('mobile', 'Call Mobile'), ('home', 'Call Home'), ('work', 'Call Work'), ('text', 'Text Mobile'), ('email', 'Email')], default='mobile', max_length=11),
        ),
    ]
