# Generated by Django 2.1.7 on 2023-06-23 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0006_auto_20190408_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='location',
        ),
    ]
