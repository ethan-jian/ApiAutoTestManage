import json
import re
from django.db import IntegrityError
from django.views.decorators.http import require_http_methods

from interface_app.forms.api_form import ApiForm
from interface_app.forms.project_form import ProjectForm
from interface_app.libs.reponse import Reponse
from interface_app.models import Project
from interface_app.models import models
from interface_app.models import Api
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


@require_http_methods(['POST'])
def add_api(request, *args, **kwargs):
    body = request.body
    data = json.loads(body, encoding='utf-8')
    print(data)
    form = ApiForm(data)
    if not form.is_valid():
        Reponse().response_failed()
    try:
        service = Api.objects.create(**form.cleaned_data)
    except IntegrityError:
        return Reponse().response_failed(message='接口已存在')
    else:
        if not service:
            return Reponse().response_failed()
        else:
            return Reponse().response_success(0, None)


@require_http_methods(['POST'])
def get_api_list_info(request, *args, **kwargs):
    """
    获取api列表
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    body = request.body
    data = json.loads(body, encoding='utf-8')
    kw = data.get('kw', '')
    current_page = data.get('currentPage', 1)
    page_size = data.get('pageSize', 10)
    sort = data.get('sort')
    prefix = ''
    if sort[0].get('direct').upper() == 'DESC':
        prefix = '-'
    order_field = prefix + sort[0].get('field')

    project_set = Project.objects.filter(name__contains=kw).order_by(order_field).values()
    total_count = len(project_set)
    paginator = Paginator(project_set, page_size)
    try:
        project_set = paginator.page(current_page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        project_set = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        project_set = paginator.page(1)

    project_list = list(project_set.object_list)


    for n in project_list:
        n['user_name'] = User.objects.get(id=n['user_id_id']).username
    project_list = Reponse().response_success(total_count, project_list)

    return project_list

@require_http_methods(['POST'])
def cat_api_detail(request, *args, **kwargs):
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
def edit_api(request, *args, **kwargs):
    """
    编辑接口
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    body = request.body
    data = json.loads(body, encoding='utf-8')
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
def delete_api(request, *args, **kwargs):

    ids = json.loads(request.body, encoding='utf-8').get('ids')
    for id in ids:
        Api.objects.filter(id=int(id)).delete()

    return Reponse().response_success(0, None)

