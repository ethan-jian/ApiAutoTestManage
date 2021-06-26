"""ApiAutoTestManage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from interface_app.views import project_view, user_view, api_view, module_view, caseSet_view, case_view

urlpatterns = [
    path(r'api/admin/', admin.site.urls),
    path(r'api/UserLogin', user_view.user_login),
    path(r'api/UserRegister', user_view.user_register),
    path(r'api/UserLogout', user_view.user_logout),
    path(r'api/LoginUserInfo', user_view.get_login_user_info),
    path(r'api/UserInfo', user_view.get_user_info),
    path(r'api/AddProject', project_view.add_project),
    path(r'api/ListProject', project_view.get_project_list_info),
    path(r'api/DetailProject', project_view.cat_project_detail),
    path(r'api/EditProject', project_view.edit_project),
    path(r'api/DeleteProject', project_view.delete_project),
    path(r'api/ProjectModule', project_view.get_project_module_list_info),
    path(r'api/ProjectCaseSet', project_view.get_project_caseSet_list_info),

    path(r'api/AddModule', module_view.add_module),
    path(r'api/ListModule', module_view.get_module_list_info),
    path(r'api/DetailModule', module_view.cat_module_detail),
    path(r'api/EditModule', module_view.edit_module),
    path(r'api/DeleteModule', module_view.delete_module),

    path(r'api/AddApi', api_view.add_api),
    path(r'api/ListApi', api_view.get_api_list_info),
    path(r'api/DetailApi', api_view.cat_api_detail),
    path(r'api/EditApi', api_view.edit_api),
    path(r'api/DeleteApi', api_view.delete_api),
    path(r'api/RunApi', api_view.run_api),

    path(r'api/AddCaseSet', caseSet_view.add_case_set),
    path(r'api/ListCaseSet', caseSet_view.get_case_set_info),
    path(r'api/DetailCaseSet', caseSet_view.cat_case_set_detail),
    path(r'api/EditCaseSet', caseSet_view.edit_case_set),
    path(r'api/DeleteCaseSet', caseSet_view.delete_case_set),

    path(r'api/AddCase', case_view.add_case),
    path(r'api/ListCase', case_view.get_case_info),
    path(r'api/DetailCase', case_view.cat_case_detail),
    path(r'api/EditCase', case_view.edit_case),
    path(r'api/DeleteCase', case_view.delete_case),

    path(r'api/AddCaseStep', case_view.add_case_step),
    path(r'api/ListCaseStep', case_view.get_case_step_info),
    path(r'api/DeleteCaseStep', case_view.delete_case_step),

]
