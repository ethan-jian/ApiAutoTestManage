# Generated by Django 2.2.2 on 2020-12-23 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interface_app', '0003_auto_20201222_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]