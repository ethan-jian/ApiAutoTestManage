# Generated by Django 2.0.1 on 2021-01-28 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interface_app', '0004_auto_20210128_2133'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='module',
            unique_together=set(),
        ),
    ]