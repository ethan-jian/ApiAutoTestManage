import json
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import IntegrityError
from interface_app.libs.reponse import Reponse
from interface_app.models import Project
from interface_app.forms.project_form import ProjectForm
from django.views.generic import View


class BaseView(View):

    Model = Project
    form = ProjectForm
    rs_list = [{}, {}]
    message = "已存在"
    add_file = 'username' #接口增加的字段
    filter_file = 'user_id' #通过过滤字段查询
    total_count = 0

    def __init__(self, request, *args, **kwargs):
        self.body = json.loads(request.body, encoding='utf-8')

    def add_view(self, request, *args, **kwargs):
        """
        新增接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        form = self.form(self.body)
        if not form.is_valid():
            Reponse().response_failed()
        try:
            service = self.Model.objects.create(**form.cleaned_data)
        except IntegrityError:
            return Reponse().response_failed(message=self.message)
        else:
            if not service:
                return Reponse().response_failed()
            else:
                return Reponse().response_success(0, None)

    def list_view(self, request, *args, **kwargs):
        """
        列表接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        kw = self.body.get('kw', '')
        current_page = self.body.get('currentPage', 1)
        page_size = self.body.get('pageSize', 10)
        sort = self.body.get('sort')
        prefix = ''
        if sort[0].get('direct').upper() == 'DESC':
            prefix = '-'
        order_field = prefix + sort[0].get('field')

        obj_set = self.Model.objects.filter(name__contains=kw).order_by(order_field).values()
        self.total_count = len(obj_set)
        paginator = Paginator(obj_set, page_size)
        try:
            obj_set = paginator.page(current_page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            obj_set = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            obj_set = paginator.page(1)

        rs_list = list(obj_set.object_list)

        self.rs_list = Reponse().response_success(self.total_count, rs_list)

        return self.rs_list


    def edit_view(self, request, *args, **kwargs):
        """
        编辑接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        id = self.body.get('id', None)
        self.body = {key: val for key, val in self.body.items() if key != 'id'}
        Project.objects.filter(id=id).update(**self.body)

        return Reponse().response_success(0, None)


    def delelte_view(self, request, *args, **kwargs):
        """
        删除接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ids = self.body.get('ids')
        for id in ids:
            self.Model.objects.filter(id=int(id)).delete()

        return Reponse().response_success(0, None)


    def detail_view(self, request, *args, **kwargs):
        """
        详情接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        id = self.body.get('id', None)
        self.total_count = 1
        if id:
            rs_set = self.Model.objects.filter(id=id).values()
            self.rs_list = Reponse().response_success(self.total_count, list(rs_set))

        return self.rs_list


    def jsonData_to_dictData(self, request, *args, **kwargs):
        """
        把返回的json类型的data转换为str类型的data
        :return:
        """
        rs_str = str(list(self.rs_list)[0], encoding="utf-8")
        rs_dict = json.loads(rs_str)

        return rs_dict


    def add_file_to_data(self, request, *args, **kwargs):
        """
        为返回的data增加字段
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        add_file = self.add_file
        filter_file = self.filter_file
        rs_dict = self.jsonData_to_dictData(request, *args, **kwargs)
        for n in rs_dict['data']:
            str_expression = """n[add_file] = self.Model.objects.get(id=n[filter_file]).%s"""%(add_file)
            exec(str_expression)
        obj_list = Reponse().response_success(self.total_count, rs_dict['data'])

        return obj_list


if __name__ == '__main__':
    pass
