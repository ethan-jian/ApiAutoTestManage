# Generated by Django 2.0.2 on 2021-06-26 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interface_app', '0017_auto_20210626_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casestepdata',
            name='case',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='interface_app.Case'),
        ),
    ]