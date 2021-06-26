# Generated by Django 2.0.2 on 2021-06-16 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interface_app', '0008_auto_20210607_2351'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='接口名称')),
                ('desc', models.CharField(blank=True, max_length=256, verbose_name='接口描述')),
                ('body_type', models.CharField(blank=True, max_length=32, verbose_name='参数类型选择')),
                ('base_url', models.CharField(blank=True, max_length=128, verbose_name='基础url,序号对应项目的环境')),
                ('up_func', models.CharField(max_length=128, verbose_name='接口执行前的函数')),
                ('down_func', models.CharField(max_length=128, verbose_name='接口执行后的函数')),
                ('method', models.CharField(blank=True, max_length=32, verbose_name='请求方式')),
                ('body_form_data', models.TextField(verbose_name='form-data形式的参数')),
                ('body_json', models.TextField(verbose_name='json形式的参数')),
                ('url_param', models.TextField(verbose_name='url上面所带的参数')),
                ('url', models.CharField(max_length=256, verbose_name='接口地址')),
                ('skip', models.CharField(blank=True, max_length=256, verbose_name='跳过判断')),
                ('extract', models.CharField(max_length=2048, verbose_name='提取信息')),
                ('validate', models.CharField(max_length=2048, verbose_name='断言信息')),
                ('header', models.CharField(max_length=2048, verbose_name='头部信息')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('api', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='interface_app.Api')),
                ('case', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='interface_app.Case')),
            ],
        ),
    ]