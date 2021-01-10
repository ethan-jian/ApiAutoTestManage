from django import forms


class ApiForm(forms.Form):
    name = forms.CharField(max_length=64,
                           min_length=1,
                           required=True)
    module_id = forms.IntegerField(required=True)
    project_id = forms.IntegerField(required=True)
    url = forms.CharField(max_length=1024, required=False)
    desc = forms.CharField(max_length=1024, required=False)
