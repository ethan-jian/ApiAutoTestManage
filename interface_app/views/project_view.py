import json
from django.db import IntegrityError
from django.views.decorators.http import require_http_methods
from interface_app.forms.project_form import ProjectForm
from interface_app.libs.reponse import Reponse
from interface_app.models import Project
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from interface_app.views.base_view import BaseView


class ProjectView(BaseView):
    Model = Project
    form = ProjectForm

@require_http_methods(['POST'])
def add_project(request, *args, **kwargs):
    obj = ProjectView()
    obj.message = "项目已存在"
    return obj.add_view(request, *args, **kwargs)


@require_http_methods(['POST'])
def get_project_list_info(request, *args, **kwargs):
    """
    获取项目列表
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    obj = ProjectView()
    obj_list = obj.list_view(request, *args, **kwargs)
    obj_str = str(list(obj_list)[0], encoding="utf-8")
    obj_dict = json.loads(obj_str)

    for n in obj_dict['data']:
        n['username'] = User.objects.get(id=n['user_id']).username
    obj_list = Reponse().response_success(obj.total_count, obj_dict['data'])

    return obj_list


@require_http_methods(['POST'])
def cat_project_detail(request, *args, **kwargs):
    """
    查询某个项目信息
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    body = request.body
    data = json.loads(body, encoding='utf-8')
    id = data.get('id', None)
    total_count = 1
    if id:
        project_set = Project.objects.filter(id=id).values()
        project_list = list(project_set)
        for n in project_list:
            n['user_name'] = User.objects.get(id=n['user_id_id']).username
        project_list = Reponse().response_success(total_count, project_list)

    return project_list


@require_http_methods(['POST'])
def edit_project(request, *args, **kwargs):
    """
    编辑项目
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    body = request.body
    data = json.loads(body, encoding='utf-8')
    print(data)
    id = data.get('id', None)
    name = data.get('name')
    test_environment = data.get('test_environment')
    dev_environment = data.get('dev_environment')
    online_environment = data.get('online_environment')
    bak_environment = data.get('bak_environment')
    environment_type = data.get('environment_type')
    principal = data.get('principal', '')
    variables = data.get('variables')
    headers = data.get('headers', '')
    func_file = data.get('func_file', '')
    desc = data.get('desc')
    user_id_id = data.get('user_id_id')
    Project.objects.filter(id=id).update(name=name,
                                         test_environment=test_environment,
                                         dev_environment=dev_environment,
                                         online_environment=online_environment,
                                         bak_environment=bak_environment,
                                         environment_type=environment_type,
                                         principal=principal,
                                         variables=variables,
                                         headers=headers,
                                         func_file=func_file,
                                         desc=desc,
                                         user_id_id=user_id_id
                                         )

    return Reponse().response_success(0, None)


@require_http_methods(['POST'])
def delete_project(request, *args, **kwargs):

    ids = json.loads(request.body, encoding='utf-8').get('ids')
    print(ids)
    for id in ids:
        Project.objects.filter(id=int(id)).delete()

    return Reponse().response_success(0, None)

