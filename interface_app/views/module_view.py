from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from interface_app.forms.module_form import ModuleForm
from interface_app.models import Module, Project
from django.contrib.auth.models import User
from interface_app.views.base_view import BaseView


class ModuleView(BaseView):

    Model = Module
    form = ModuleForm
    add_file_k = 'project_name'  # 接口增加的字段名k
    filter_file = 'project_id'  # 通过过滤字段查询
    total_count = 0


@require_http_methods(['POST'])
def add_module(request, *args, **kwargs):
    obj = ModuleView(request, *args, **kwargs)
    obj.message = "已存在"

    return obj.add_view(request, *args, **kwargs)


@require_http_methods(['POST'])
@login_required
def get_module_list_info(request, *args, **kwargs):
    """
    获取列表
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    obj = ModuleView(request, *args, **kwargs)
    orm_sql = "models.Module.objects.filter(project__name__contains=self.kw)." \
              "extra(select={'%s': 'select name from interface_app_project where id = project_id'})." \
              "values().order_by(self.order_field)" % obj.add_file_k

    return obj.list_view(request, *args, **{"orm_sql": orm_sql})


@require_http_methods(['POST'])
def cat_module_detail(request, *args, **kwargs):
    """
    查询某个信息
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    obj = ModuleView(request, *args, **kwargs)
    orm_sql = "models.Module.objects.filter(id=id)" \
              ".extra(select={'%s': 'select name from interface_app_project where id = project_id'}).values()" % (obj.add_file_k)

    return obj.detail_view(request, *args, **{"orm_sql": orm_sql})


@require_http_methods(['POST'])
def edit_module(request, *args, **kwargs):
    """
    编辑
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    obj = ModuleView(request, *args, **kwargs)

    return obj.edit_view(request, *args, **kwargs)


@require_http_methods(['POST'])
def delete_module(request, *args, **kwargs):
    """
    删除
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    obj = ModuleView(request, *args, **kwargs)

    return obj.delelte_view(request, *args, **kwargs)

