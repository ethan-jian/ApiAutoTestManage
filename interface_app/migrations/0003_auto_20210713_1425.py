# Generated by Django 2.0.1 on 2021-07-13 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface_app', '0002_auto_20210713_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casestepdata',
            name='num',
            field=models.IntegerField(blank=True, default=1000000000, verbose_name='接口序号'),
        ),
    ]
