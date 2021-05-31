import json

from django.db.models import F
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from flask.json import JSONEncoder

from interface_app.libs.reponse import Reponse
from interface_app import models
from interface_app.forms.api_form import ApiForm
from interface_app.forms.module_form import ModuleForm
from interface_app.models import Api, Project
from django.contrib.auth.models import User

from interface_app.util.http_run import Run
from interface_app.util.utils import encode_object
from interface_app.views.base_view import BaseView
from interface_app.libs.httprunner.api import HttpRunner

response = Reponse()


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


@require_http_methods(['POST'])
def run_api(request, *args, **kwargs):
    """
    跑单个接口
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    body = json.loads(request.body, encoding='utf-8')
    name = body['name']
    base_url = body['baseUrl']
    up_func = body['upGunc']
    body_form_data = body['upFunc']
    body_json = body['bodyJson']
    method = body['method']
    url_param = body['urlParam']
    url = body['url']
    skip = body['skip']
    extract = body['extract']
    validate = body['validate']
    header = body['header']
    down_func = body['downFunc']
    project_id = body['projectId']
    api_data = models.Project.objects.filter(id=project_id).values("variables")
    api_data = list(api_data)[0]
    variables = {n['key']: n['value'] for n in json.loads(api_data['project__variables'])}
    test_data = {
        "testcases": [
            {
                "teststeps": [
                    {
                        "name": name,
                        "request": {
                            "method": method,
                            "files": {

                            },
                            "data": {

                            },
                            "url": base_url + url,
                            "params": {

                            },
                            "headers": {

                            },
                            "json": json.loads(body_json)

                        },
                        "extract": extract,

                        "validate": validate,
                    }
                ],
                "config": {
                    "variables": {

                    }
                }
            }
        ],
        "project_mapping": {
            "functions": {
            },

            "variables": variables
        }
    }

    runner = HttpRunner()

    runner.run(test_data)
    jump_res = json.dumps(runner._summary, ensure_ascii=False, default=encode_object, cls=JSONEncoder)
    print(jump_res)
    return jump_res


    return response.response_success(totalCount=1, data=api_data)


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
              ".extra(select={'%s': 'select name from interface_app_project where id = project_id'}).values()" % (
                  obj.add_file_k)

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
