# Generated by Django 2.2.2 on 2020-12-10 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0, verbose_name='userid')),
                ('name', models.CharField(blank=True, default='', max_length=64, unique=True, verbose_name='项目名称')),
                ('host', models.CharField(blank=True, max_length=1024, verbose_name='测试环境')),
                ('host_two', models.CharField(max_length=1024, verbose_name='开发环境')),
                ('host_three', models.CharField(max_length=1024, verbose_name='线上环境')),
                ('host_four', models.CharField(max_length=1024, verbose_name='备用环境')),
                ('environment_choice', models.CharField(max_length=16, verbose_name='环境选择，first为测试，以此类推')),
                ('principal', models.CharField(blank=True, max_length=16)),
                ('variables', models.CharField(max_length=2048, verbose_name='项目的公共变量')),
                ('headers', models.CharField(max_length=1024, verbose_name='项目的公共头部信息')),
                ('func_file', models.CharField(blank=True, max_length=64, unique=True, verbose_name='函数文件')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]