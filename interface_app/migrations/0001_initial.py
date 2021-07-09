# Generated by Django 2.0.1 on 2021-07-09 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
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
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(blank=True, default=1, verbose_name='用例序号')),
                ('name', models.CharField(max_length=128, verbose_name='用例名称')),
                ('desc', models.CharField(blank=True, max_length=256, verbose_name='用例描述')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CaseSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='用例集名称')),
                ('desc', models.CharField(max_length=1024, verbose_name='用例集描述')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CaseStepData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(blank=True, default=1, verbose_name='接口序号')),
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
                ('api', models.ForeignKey(db_constraint=False, default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='interface_app.Api')),
                ('case', models.ForeignKey(db_constraint=False, default=1, on_delete=django.db.models.deletion.CASCADE, to='interface_app.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='项目名称')),
                ('desc', models.CharField(max_length=1024, verbose_name='项目描述')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='项目名称')),
                ('test_environment', models.CharField(blank=True, max_length=1024, verbose_name='测试环境')),
                ('dev_environment', models.CharField(blank=True, max_length=1024, verbose_name='开发环境')),
                ('online_environment', models.CharField(blank=True, max_length=1024, verbose_name='线上环境')),
                ('bak_environment', models.CharField(blank=True, max_length=1024, verbose_name='备用环境')),
                ('environment_type', models.CharField(max_length=1, verbose_name='环境标识')),
                ('principal', models.CharField(blank=True, max_length=16)),
                ('variables', models.CharField(max_length=2048, verbose_name='项目的公共变量')),
                ('headers', models.CharField(max_length=1024, verbose_name='项目的公共头部信息')),
                ('func_file', models.CharField(blank=True, max_length=64, verbose_name='函数文件')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('desc', models.CharField(max_length=1024, verbose_name='项目描述')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_diff1', to='interface_app.Project'),
        ),
        migrations.AddField(
            model_name='caseset',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_diff3', to='interface_app.Project'),
        ),
        migrations.AddField(
            model_name='case',
            name='case_set',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='interface_app.CaseSet'),
        ),
        migrations.AddField(
            model_name='case',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_diff4', to='interface_app.Project'),
        ),
        migrations.AddField(
            model_name='api',
            name='module',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='interface_app.Module'),
        ),
        migrations.AddField(
            model_name='api',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_diff2', to='interface_app.Project'),
        ),
        migrations.AlterUniqueTogether(
            name='module',
            unique_together={('name', 'project')},
        ),
        migrations.AlterUniqueTogether(
            name='caseset',
            unique_together={('name', 'project')},
        ),
        migrations.AlterUniqueTogether(
            name='case',
            unique_together={('name', 'case_set', 'project')},
        ),
        migrations.AlterUniqueTogether(
            name='api',
            unique_together={('name', 'module', 'project')},
        ),
    ]
