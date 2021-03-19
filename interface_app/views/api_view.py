import json

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from flask.json import JSONEncoder

from interface_app.forms.api_form import ApiForm
from interface_app.forms.module_form import ModuleForm
from interface_app.models import Api, Project
from django.contrib.auth.models import User
from interface_app.views.base_view import BaseView
from interface_app.libs.httprunner.api import HttpRunner

class ApiView(BaseView):

    Model = Api
    form = ApiForm
    add_file_k = 'project_name'  # 接口增加的字段名k
    filter_file = 'project_id'  # 通过过滤字段查询
    total_count = 0


@require_http_methods(['POST'])
@login_required
def add_api(request, *args, **kwargs):
    obj = ApiView(request, *args, **kwargs)
    obj.message = "已存在"

    return obj.add_view(request, *args, **kwargs)


@require_http_methods(['GET'])
@login_required
def run_api(request, *args, **kwargs):
    # obj = ApiView(request, *args, **kwargs)
    # obj.message = "已存在"
    # data = {"testcases": [{"teststeps": [{"name": "登录/Login/login", "request": {"method": "POST", "files": {}, "data": {}, "url": "http://123.56.107.182:21001/Login/login", "params": {}, "headers": {}, "json": {"loginName": "$loginName", "passWord": "$passWord"}}, "extract": [{"token": "content.data"}, {"code1": "content.code"}, {"message1": "content.message"}], "validate": [{"equals": ["status_code", 200]}, {"equals": ["$code1", 200]}, {"equals": ["$message1", "操作成功"]}]}], "config": {"variables": {}}}], "project_mapping": {"functions": {}, "variables": {"loginName": "administrator", "passWord": "123456", "Accept": "application/json, text/plain, */*", "Content-Type": "application/json;charset=UTF-8", "addRobot": "addRobot", "addRobtGroup": "addRobtGroup", "modifyRobot": "modifyRobot", "modifyRobotGroup": "modifyRobotGroup", "addmachineName": "addmachineName", "adddescription": "adddescription", "addsystemLoginName": "addsystemLoginName", "addsystemPassword": "addsystemPassword", "modifysystemPassword": "modifysystemPassword", "modifydescription": "modifydescription", "modifymachineName": "modifymachineName", "modifysystemLoginName": "modifysystemLoginName", "addRobtGroupDescription": "addRobtGroupDescription", "modifyRobtGroupDescription": "modifyRobtGroupDescription", "file_path": r"C:\\Users\\ethan\\Desktop\\上传\\参数测试1030.nupkg", "filename": "参数测试1030.nupkg"}}}
    data = {'testcases': [{'teststeps': [{'name': '获取token/connect/token', 'request': {'method': 'POST', 'files': {}, 'data': {'client_id': 'wpfclient', 'client_secret': '49C1A7E1-0C79-4A89-A3D6-A37998FB86B0', 'grant_type': 'password', 'username': '13723418945', 'password': 'as123456'}, 'url': 'http://123.56.107.182:12001/connect/token', 'params': {}, 'headers': {}}, 'extract': [], 'validate': []}], 'config': {'variables': {}}}], 'project_mapping': {'functions': {}, 'variables': {'username': '13723418945', 'password': 'as123456', 'Accept': 'application/json, text/plain, */*', 'Content-Type': 'application/json;charset=UTF-8'}}}
    obj = HttpRunner()
    obj.run(data)
    jump_res = json.dumps(obj._summary, ensure_ascii=False, cls=JSONEncoder)
    print(jump_res)

    return jump_res


@require_http_methods(['POST'])
@login_required
def get_api_list_info(request, *args, **kwargs):
    """
    获取列表
    :param request:
    :param args:
    :param kwargs:
    :return:
    """

    obj = ApiView(request, *args, **kwargs)
    project_id = obj.body.get('project_id')
    module_id = obj.body.get('module_id')
    print(project_id, module_id)
    if project_id and module_id:
        filter_expression = "Q(project_id=%s) & Q(module_id=%s)" % (project_id, module_id)
    elif project_id:
        filter_expression = "Q(project_id=%s)" % (project_id)
    elif not project_id and not module_id:
        filter_expression = "project__name__contains=self.kw"

    orm_sql = "models.Api.objects.filter(%s)." \
              "extra(select={'project_name': 'select name from interface_app_project where id = project_id'," \
              "'module_name': 'select name from interface_app_module where id = module_id'})." \
              "values().order_by(self.order_field)" % filter_expression

    return obj.list_view(request, *args, **{"orm_sql": orm_sql})


@require_http_methods(['POST'])
def cat_api_detail(request, *args, **kwargs):
    """
    查询某个信息
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    obj = ApiView(request, *args, **kwargs)
    orm_sql = "models.Api.objects.filter(id=id)" \
              ".extra(select={'%s': 'select name from interface_app_project where id = project_id'}).values()" % (obj.add_file_k)

    return obj.detail_view(request, *args, **{"orm_sql": orm_sql})


@require_http_methods(['POST'])
def edit_api(request, *args, **kwargs):
    """
    编辑
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    obj = ApiView(request, *args, **kwargs)

    return obj.edit_view(request, *args, **kwargs)


@require_http_methods(['POST'])
def delete_api(request, *args, **kwargs):
    """
    删除
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    obj = ApiView(request, *args, **kwargs)

    return obj.delelte_view(request, *args, **kwargs)

