# Generated by Django 5.0.9 on 2024-11-08 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_os_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goldenimage',
            name='weight',
            field=models.PositiveSmallIntegerField(default=1000),
        ),
    ]
