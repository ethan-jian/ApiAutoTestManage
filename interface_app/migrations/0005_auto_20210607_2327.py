# Generated by Django 2.0.2 on 2021-06-07 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interface_app', '0004_auto_20210204_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case_set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='用例集名称')),
                ('desc', models.CharField(max_length=1024, verbose_name='用例集描述')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='interface_app.Project')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='case_set',
            unique_together={('name', 'project')},
        ),
    ]