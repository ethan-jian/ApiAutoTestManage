from django.db import models
from django.contrib.auth.models import User
#
#
# # class Publish(models.Model):
# #     name = models.CharField(max_length=64)
# #     city = models.CharField(max_length=63, null=True)
# #
# #     def __str__(self):
# #         return self.name
# #
# #
# # class Author(models.Model):
# #     name = models.CharField(max_length=30)
# #     sex = models.CharField(max_length=20)
# #
# #     def __str__(self):
# #         return self.name
# #
# #
# # class Book(models.Model):
# #     title = models.CharField(max_length=64)
# #     price = models.IntegerField()
# #     color = models.CharField(max_length=64)
# #     page_num = models.IntegerField(null=True)
# #     publisher = models.ForeignKey("Publish", on_delete=models.CASCADE,
# #                                   null=True)  # 一对多的关系。2.0django中，当有主外键和其他对应关系时，需要设置。
# #     author = models.ManyToManyField("Author")
# #
# #     def __str__(self):
# #         return self.title
#
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

    name = models.CharField('项目名称', blank=False, max_length=64, unique=True)
    porject = models.ForeignKey(Project, to_field='id', default=1, on_delete=models.DO_NOTHING)
    desc = models.CharField('项目描述', max_length=1024)

class Api(models.Model):

    name = models.CharField('接口名称', blank=False, max_length=64, unique=True)
    url = models.CharField('接口地址', blank=False, max_length=64, unique=False)
    desc = models.CharField('接口描述', max_length=1024)
    module = models.ForeignKey(Module, to_field='id', default=1, on_delete=models.DO_NOTHING)
    project = models.ForeignKey(Project, to_field='id', default=1, on_delete=models.DO_NOTHING)


#
# #
# # class Module(models):
# #     name = models.CharField('接口模块', max_length=64, blank=True)
# #     num = models.IntegerField('模块序号', blank=True)
# #     project_id = models.ForeignKey('Project', related_name='id', on_delete=models.CASCADE())
# #     api_msg = db.relationship('ApiMsg', order_by='ApiMsg.num.asc()', lazy='dynamic')
# #     created_time = db.Column(db.DateTime, index=True, default=datetime.now, comment='创建时间')
# #     update_time = db.Column(db.DateTime, index=True, default=datetime.now, onupdate=datetime.now)
# #
# #
# # class Config(models):
# #     id = db.Column(db.Integer(), primary_key=True, comment='主键，自增')
# #     num = db.Column(db.Integer(), nullable=True, comment='配置序号')
# #     name = db.Column(db.String(128), comment='配置名称')
# #     variables = db.Column(db.String(21000), comment='配置参数')
# #     func_address = db.Column(db.String(128), comment='配置函数')
# #     project_id = db.Column(db.Integer, db.ForeignKey('project.id'), comment='所属的项目id')
# #     created_time = db.Column(db.DateTime, index=True, default=datetime.now, comment='创建时间')
# #     update_time = db.Column(db.DateTime, index=True, default=datetime.now, onupdate=datetime.now)
# #
# #
# # class CaseSet(models):
# #     id = db.Column(db.Integer(), primary_key=True, comment='主键，自增')
# #     num = db.Column(db.Integer(), nullable=True, comment='用例集合序号')
# #     name = db.Column(db.String(256), nullable=True, comment='用例集名称')
# #     project_id = db.Column(db.Integer, db.ForeignKey('project.id'), comment='所属的项目id')
# #     cases = db.relationship('Case', order_by='Case.num.asc()', lazy='dynamic')
# #     created_time = db.Column(db.DateTime, index=True, default=datetime.now, comment='创建时间')
# #     update_time = db.Column(db.DateTime, index=True, default=datetime.now, onupdate=datetime.now)
# #
# #
#
