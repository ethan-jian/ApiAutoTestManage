# Generated by Django 2.0.1 on 2021-01-29 08:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('interface_app', '0006_auto_20210128_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='method',
            field=models.CharField(default=django.utils.timezone.now, max_length=64, verbose_name='请求方法'),
            preserve_default=False,
        ),
    ]
