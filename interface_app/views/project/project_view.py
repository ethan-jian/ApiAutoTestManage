import json
from django.views.decorators.http import require_http_methods
from interface_app.forms.project_form import ProjectForm
from interface_app.libs.reponse import Reponse
from interface_app.models import Project


@require_http_methods(['POST'])
def add_project(requset, *args, **kwargs):
    body = requset.body
    data = json.loads(body, encoding='utf-8')
    print(data)
    form = ProjectForm(data)
    if not form.is_valid():
        Reponse().response_failed()

    service = Project.objects.create(**form.cleaned_data)
    if not service:
        return Reponse().response_failed()
    else:
        return Reponse().response_success(0, None)




@require_http_methods(['POST'])
def edit_project(requset, *args, **kwargs):
    pass


@require_http_methods(['POST'])
def delete_project(requset, *args, **kwargs):
    pass


