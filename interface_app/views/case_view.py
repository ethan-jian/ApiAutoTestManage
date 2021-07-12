import json

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.http import require_http_methods
from interface_app import models
from interface_app.forms.case_data_form import CaseDataForm
from interface_app.forms.case_form import CaseForm
from interface_app.models import Case, CaseStepData, Api
from interface_app.views.base_view import BaseView
from interface_app.libs.reponse import Reponse
from django.http import JsonResponse


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
def add_case_step(request, *args, **kwargs):
    bodys = json.loads(request.body, encoding='utf-8')
    api_id_list = bodys.get('api_id_list')
    case_id = bodys.get('case_id')
    case_step_list = []
    for api_id in api_id_list:
        api_set = models.Api.objects.filter(id=api_id).values("id", "name", "desc", "body_type", "base_url", "up_func",
                                                              "down_func", "method", "body_form_data", "body_json",
                                                              "url_param", "url", "skip", "extract", "validate",
                                                              "header"
                                                              )
        api_list = list(api_set)
        api_list[0]["api_id"] = api_list[0].pop("id")
        api_list[0]["case_id"] = case_id
        case_step_list = case_step_list + api_list

    case_steps = []
    for case_step in case_step_list:
        case_steps.append(CaseStepData(**case_step))
    CaseStepData.objects.bulk_create(case_steps)
    totalCount = len(case_steps)

    return Reponse().response_success(totalCount, data=None)


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
    project_id = body.get('project_id', '')
    case_set_id = body.get('case_set_id', '')
    current_page = body.get('currentPage', '')
    page_size = body.get('pageSize', '')
    sort = body.get('sort')
    prefix = ''
    if sort[0].get('direct').upper() == 'DESC':
        prefix = '-'
    order_field = prefix + sort[0].get('field')
    obj_set = models.Case.objects.filter(project_id=project_id).filter(case_set_id=case_set_id).values().order_by(
        order_field)

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
def get_case_step_info(request, *args, **kwargs):
    """
    获取列表
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    obj = CaseView(request, *args, **kwargs)
    obj.Model = CaseStepData
    orm_sql = "models.CaseStepData.objects.filter(case_id=self.kw).values().order_by(self.order_field)"

    return obj.list_view(request, *args, **{"orm_sql": orm_sql})



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
              ".extra(select={'%s': 'select name from interface_app_project where id = project_id'}).values()" % (
                  obj.add_file_k)

    return obj.detail_view(request, *args, **{"orm_sql": orm_sql})


@require_http_methods(['POST'])
def cat_case_step_detail(request, *args, **kwargs):
    """
    查询某个信息
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    obj = CaseView(request, *args, **kwargs)
    obj.Model = CaseStepData
    orm_sql = "models.CaseStepData.objects.filter(id=id).values()"

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
def edit_case_step_info(request, *args, **kwargs):
    """
    编辑
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    obj = CaseView(request, *args, **kwargs)
    obj.Model = CaseStepData

    return obj.edit_view(request, *args, **kwargs)


@require_http_methods(['POST'])
def bulk_edit_case_step_info(request, *args, **kwargs):
    """
    批量编辑
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    obj = CaseView(request, *args, **kwargs)
    obj.Model = CaseStepData

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


@require_http_methods(['POST'])
def delete_case_step(request, *args, **kwargs):
    """
    删除
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    obj = CaseView(request, *args, **kwargs)
    obj.Model = CaseStepData

    return obj.delelte_view(request, *args, **kwargs)
