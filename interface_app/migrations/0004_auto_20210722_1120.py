# Generated by Django 2.0.1 on 2021-07-22 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface_app', '0003_auto_20210713_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='update_time',
            field=models.DateTimeField(),
        ),
    ]