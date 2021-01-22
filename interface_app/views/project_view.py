from django.views.decorators.http import require_http_methods
from interface_app.forms.project_form import ProjectForm
from interface_app.models import Project
from django.contrib.auth.models import User
from interface_app.views.base_view import BaseView


class ProjectView(BaseView):

    Model = Project
    form = ProjectForm
    add_file = 'username' #接口增加的字段
    filter_file = 'user_id' #通过过滤字段查询
    total_count = 0


@require_http_methods(['POST'])
def add_project(request, *args, **kwargs):
    obj = ProjectView(request, *args, **kwargs)
    obj.message = "已存在"

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
    obj = ProjectView(request, *args, **kwargs)
    obj.list_view(request, *args, **kwargs)
    obj.Model = User

    return obj.add_file_to_data(request, *args, **kwargs)


@require_http_methods(['POST'])
def cat_project_detail(request, *args, **kwargs):
    """
    查询某个项目信息
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    obj = ProjectView(request, *args, **kwargs)
    obj.detail_view(request, *args, **kwargs)
    obj.Model = User

    return obj.add_file_to_data(request, *args, **kwargs)


@require_http_methods(['POST'])
def edit_project(request, *args, **kwargs):
    """
    编辑项目
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    obj = ProjectView(request, *args, **kwargs)

    return obj.edit_view(request, *args, **kwargs)


@require_http_methods(['POST'])
def delete_project(request, *args, **kwargs):
    """
    删除项目
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    obj = ProjectView(request, *args, **kwargs)

    return obj.delelte_view(request, *args, **kwargs)
