from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):

    name = models.CharField('项目名称', blank=False, max_length=64, unique=True)
    test_environment = models.CharField('测试环境', max_length=1024, blank=True)
    dev_environment = models.CharField('开发环境', max_length=1024, blank=True)
    online_environment = models.CharField('线上环境', max_length=1024, blank=True)
    bak_environment = models.CharField('备用环境', max_length=1024, blank=True)
    environment_type = models.CharField('环境标识', max_length=1, blank=False)
    principal = models.CharField(max_length=16, blank=True)
    variables = models.CharField('项目的公共变量', max_length=2048)
    headers = models.CharField('项目的公共头部信息', max_length=1024)
    func_file = models.CharField('函数文件', max_length=64, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    desc = models.CharField('项目描述', max_length=1024)
    user = models.ForeignKey(User, to_field='id', default=1, on_delete=models.DO_NOTHING)


class Module(models.Model):

    name = models.CharField('项目名称', blank=False, max_length=64, unique=False)
    desc = models.CharField('项目描述', max_length=1024)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, to_field='id', default=1, related_name='project_diff1', on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('name', 'project')


class Api(models.Model):

    # num = models.IntegerField('接口序号', blank=True)
    name = models.CharField('接口名称',  max_length=128, blank=False)
    desc = models.CharField('接口描述', max_length=256, blank=True)
    body_type = models.CharField('参数类型选择', max_length=32, blank=True)
    base_url = models.CharField('基础url,序号对应项目的环境', max_length=128, blank=True)
    up_func = models.CharField('接口执行前的函数', max_length=128)
    down_func = models.CharField('接口执行后的函数', max_length=128)
    method = models.CharField('请求方式', max_length=32, blank=True)
    body_form_data = models.TextField('form-data形式的参数')
    body_json = models.TextField('json形式的参数')
    url_param = models.TextField('url上面所带的参数')
    url = models.CharField('接口地址', max_length=256, blank=False)
    skip = models.CharField('跳过判断', max_length=256, blank=True)
    extract = models.CharField('提取信息', max_length=2048)
    validate = models.CharField('断言信息', max_length=2048)
    header = models.CharField('头部信息', max_length=2048)
    module = models.ForeignKey(Module, to_field='id', default=1, on_delete=models.DO_NOTHING)
    project = models.ForeignKey(Project, to_field='id', default=1, related_name='project_diff2', on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('name', 'module', 'project')


class CaseSet(models.Model):

    name = models.CharField('用例集名称', blank=False, max_length=64, unique=False)
    desc = models.CharField('用例集描述', max_length=1024)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, to_field='id', default=1, related_name='project_diff3', on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('name', 'project')


class Case(models.Model):

    name = models.CharField('用例名称',  max_length=128, blank=False)
    desc = models.CharField('用例描述', max_length=256, blank=True)
    project = models.ForeignKey(Project, to_field='id', default=1, related_name='project_diff4', on_delete=models.DO_NOTHING)
    case_set = models.ForeignKey(CaseSet, to_field='id', default=1, on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('name', 'case_set', 'project')


class CaseStepData(models.Model):

    # num = models.IntegerField('接口序号', blank=True)
    name = models.CharField('接口名称',  max_length=128, blank=False)
    desc = models.CharField('接口描述', max_length=256, blank=True)
    body_type = models.CharField('参数类型选择', max_length=32, blank=True)
    base_url = models.CharField('基础url,序号对应项目的环境', max_length=128, blank=True)
    up_func = models.CharField('接口执行前的函数', max_length=128)
    down_func = models.CharField('接口执行后的函数', max_length=128)
    method = models.CharField('请求方式', max_length=32, blank=True)
    body_form_data = models.TextField('form-data形式的参数')
    body_json = models.TextField('json形式的参数')
    url_param = models.TextField('url上面所带的参数')
    url = models.CharField('接口地址', max_length=256, blank=False)
    skip = models.CharField('跳过判断', max_length=256, blank=True)
    extract = models.CharField('提取信息', max_length=2048)
    validate = models.CharField('断言信息', max_length=2048)
    header = models.CharField('头部信息', max_length=2048)
    case = models.ForeignKey(Case, to_field='id', default=1, on_delete=models.CASCADE, db_constraint=False)
    api = models.ForeignKey(Api, to_field='id', default=1, on_delete=models.DO_NOTHING, db_constraint=False)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    # class Meta:
    #     unique_together = ('name', 'module', 'project')