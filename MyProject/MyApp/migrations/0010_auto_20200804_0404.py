# Generated by Django 3.0.7 on 2020-08-04 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0009_auto_20200804_0402'),
    ]

    operations = [
        migrations.RenameField(
            model_name='main',
            old_name='age',
            new_name='YOB',
        ),
    ]
