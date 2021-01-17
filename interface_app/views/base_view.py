import json

from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import IntegrityError
from interface_app.libs.reponse import Reponse
from interface_app.models import Project
from interface_app.forms.project_form import ProjectForm
from django.views.generic import View


class BaseView(View):

    Model = Project
    form = ProjectForm
    message = "项目已存在"

    def add_view(self, request, *args, **kwargs):
        """
        新增接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.body = json.loads(request.body, encoding='utf-8')
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
        self.body = json.loads(request.body, encoding='utf-8')
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

        obj_list = list(obj_set.object_list)

        obj_list = Reponse().response_success(self.total_count, obj_list)

        return obj_list


    def edit_view(self):
        pass

    def delelte_view(self):
        pass

    def detail_view(self):
        pass

    def jsonData_to_strData(self, request, *args, **kwargs):
        """
        把返回的json类型的data转换为str类型的data
        :return:
        """
        rs_json = self.list_view(request, *args, **kwargs)
        data_str = str(list(kwargs[''])[0], encoding="utf-8")
        obj_dict = json.loads(obj_str)

        return data_str


    def add_file(self, request, *args, **kwargs):
        """
        为返回的data增加字段
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        obj_list = self.list_view(request, *args, **kwargs)
        obj_str = str(list(obj_list)[0], encoding="utf-8")
        obj_dict = json.loads(obj_str)

        for n in obj_dict['data']:
            n['user_name'] = User.objects.get(id=n['user_id_id']).username
        obj_list = Reponse().response_success(self.total_count, obj_dict['data'])

        return obj_list


if __name__ == '__main__':
    pass






if __name__ == '__main__':
    pass
