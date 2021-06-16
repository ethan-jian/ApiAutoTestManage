import json

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.http import require_http_methods
from interface_app import models
from interface_app.forms.case_form import CaseForm
from interface_app.models import Case, CaseData
from interface_app.views.base_view import BaseView
from interface_app.libs.reponse import Reponse


class CaseView(BaseView):

    Model = Case
    form = CaseForm
    add_file_k = 'project_name'  # 接口增加的字段名k
    filter_file = 'project_id'  # 通过过滤字段查询
    total_count = 0


@require_http_methods(['POST'])
@login_required
def add_case(request, *args, **kwargs):
    obj = CaseView(request, *args, **kwargs)
    obj.message = "已存在"

    return obj.add_view(request, *args, **kwargs)


@require_http_methods(['POST'])
@login_required
def add_case_data(request, *args, **kwargs):
    obj = CaseView(request, *args, **kwargs)

    obj.message = "已存在"
    obj.Model = CaseData
    obj.form = CaseForm

    return obj.add_view(request, *args, **kwargs)


@require_http_methods(['POST'])
@login_required
def get_case_info(request, *args, **kwargs):
    """
    获取列表
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    body = json.loads(request.body, encoding='utf-8')
    project_id =body.get('project_id', '')
    case_set_id = body.get('case_set_id', '')
    current_page = body.get('currentPage', '')
    page_size = body.get('pageSize', '')
    sort = body.get('sort')
    prefix = ''
    if sort[0].get('direct').upper() == 'DESC':
        prefix = '-'
    order_field = prefix + sort[0].get('field')
    obj_set = models.Case.objects.filter(project_id=project_id).filter(case_set_id=case_set_id).values().order_by(order_field)

    if current_page and page_size:
        paginator = Paginator(obj_set, page_size)
        try:
            obj_set = paginator.page(current_page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            obj_set = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            obj_set = paginator.page(1)
        obj_set = obj_set.object_list
    total_count = len(obj_set)
    rs_list = Reponse().response_success(total_count, list(obj_set))


    return rs_list


@require_http_methods(['POST'])
def cat_case_detail(request, *args, **kwargs):
    """
    查询某个信息
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    obj = CaseView(request, *args, **kwargs)
    orm_sql = "models.Case.objects.filter(id=id)" \
              ".extra(select={'%s': 'select name from interface_app_project where id = project_id'}).values()" % (obj.add_file_k)

    return obj.detail_view(request, *args, **{"orm_sql": orm_sql})


@require_http_methods(['POST'])
def edit_case(request, *args, **kwargs):
    """
    编辑
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    obj = CaseView(request, *args, **kwargs)

    return obj.edit_view(request, *args, **kwargs)


@require_http_methods(['POST'])
def delete_case(request, *args, **kwargs):
    """
    删除
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    obj = CaseView(request, *args, **kwargs)

    return obj.delelte_view(request, *args, **kwargs)

