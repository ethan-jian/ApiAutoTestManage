# Generated by Django 2.0.1 on 2021-01-28 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interface_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='api',
            unique_together={('name', 'module', 'project')},
        ),
    ]