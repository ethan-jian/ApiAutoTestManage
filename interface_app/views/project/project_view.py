import json
import re
from django.db import IntegrityError
from django.views.decorators.http import require_http_methods
from interface_app.forms.project_form import ProjectForm
from interface_app.libs.reponse import Reponse
from interface_app.models import Project
from django.contrib.auth.models import User


@require_http_methods(['POST'])
def add_project(requset, *args, **kwargs):
    body = requset.body
    data = json.loads(body, encoding='utf-8')
    print(data)
    form = ProjectForm(data)
    if not form.is_valid():
        Reponse().response_failed()
    try:
        service = Project.objects.create(**form.cleaned_data)
    except IntegrityError:
        return Reponse().response_failed(message='项目已存在')
    else:
        if not service:
            return Reponse().response_failed()
        else:
            return Reponse().response_success(0, None)


@require_http_methods(['GET'])
def get_project_list_info(request, *args, **kwargs):
    """
    获取项目列表
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    project_list = Project.objects.all().values()
    project_list = list(project_list)
    for n in project_list:
        n['user_name'] = User.objects.get(id=n['user_id_id']).username
    total = len(project_list)
    if not project_list:
        return Reponse().response_failed()
    else:
        project_list = Reponse().response_success(total, project_list)

    return project_list


@require_http_methods(['POST'])
def edit_project(requset, *args, **kwargs):
    pass


@require_http_methods(['POST'])
def delete_project(requset, *args, **kwargs):

    ids = json.loads(requset.body, encoding='utf-8').get('ids')
    print(ids)
    for id in ids:
        Project.objects.filter(id=int(id)).delete()

    return Reponse().response_success(0, None)

