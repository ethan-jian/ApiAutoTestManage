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

from interface_app.views.project import project_view
from interface_app.views.user import user_view

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'api/user/login/', user_view.user_login),
    path(r'api/user/register/', user_view.user_register),
    path(r'api/user/logout/', user_view.user_logout),
    path(r'api/user/info/', user_view.get_user_info),
    path(r'api/add/project/', project_view.add_project),
]
