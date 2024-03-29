import json
from datetime import datetime

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import IntegrityError
from django.db.models import Q
from interface_app import models
from interface_app.libs.reponse import Reponse
from interface_app.models import Project, Module
from interface_app.forms.project_form import ProjectForm
from django.views.generic import View
from django.db import connection
import os



class BaseView(Reponse):

    Model = Project
    form = ProjectForm
    rs_list = [{}, {}]
    message = "已存在"
    add_file_k = 'username' #接口增加的字段名k
    total_count = 0
    kw = ''
    order_field = ''

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
            pass
        #     print("ookoko")
        #     self.response_failed()
        try:
            service = self.Model.objects.create(**form.cleaned_data)
        except IntegrityError:
            return self.response_failed(message=self.message)
        else:
            if not service:
                return self.response_failed()
            else:
                return self.response_success(0, {"id": service.id})

    def list_view(self, request, *args, **kwargs):
        """
        列表接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.test()
        self.kw = self.body.get('kw', '')
        current_page = self.body.get('currentPage', '')
        page_size = self.body.get('pageSize', '')
        sort = self.body.get('sort')
        prefix = ''
        if sort[0].get('direct').upper() == 'DESC':
            prefix = '-'
        self.order_field = prefix + sort[0].get('field')
        obj_set = eval(kwargs.get('orm_sql', ''))

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
        self.total_count = len(obj_set)
        self.rs_list = self.response_success(self.total_count, list(obj_set))
        print(self.rs_list)

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
        self.Model.objects.filter(id=id).update(**self.body, update_time=datetime.now())

        return self.response_success(0, None)


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

        return self.response_success(0, None)


    def detail_view(self, request, *args, **kwargs):
        """
        详情接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # self.test()
        id = self.body.get('id', None)
        if id:
            obj_set = eval(kwargs.get('orm_sql', ''))
            self.total_count = len(obj_set)
            self.rs_list = self.response_success(self.total_count, list(obj_set))

        return self.rs_list


    def execute_sql(self, sql=""):
        """
        执行原生sql
        :return:
        """
        cursor = connection.cursor()
        cursor.execute(sql)
        rs = cursor.fetchall()

        return rs


    def test(self):
        pass
        # rs = models.Case.objects.filter(project_id=1).filter(case_set_id=1).values().order_by(self.order_field)
        # print(rs)
        # orm_sql = models.Api.objects.filter(Q(project_id=1) & Q(module_id="")).values()
        # print(orm_sql)



if __name__ == '__main__':
    pass

