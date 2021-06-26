# Generated by Django 2.0.1 on 2021-06-17 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interface_app', '0009_casedata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casedata',
            name='api',
            field=models.ForeignKey(db_constraint=False, default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='interface_app.Api'),
        ),
        migrations.AlterField(
            model_name='casedata',
            name='case',
            field=models.ForeignKey(db_constraint=False, default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='interface_app.Case'),
        ),
    ]