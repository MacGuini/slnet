# Generated by Django 4.0.3 on 2022-05-16 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_alter_service_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='featured',
            field=models.CharField(choices=[('featured', 'Featured'), ('other', 'Other'), ('none', 'None')], default='none', max_length=9),
        ),
    ]