from django import forms


class ApiForm(forms.Form):
    # num = forms.IntegerField(required=False)
    name = forms.CharField(max_length=64,
                           min_length=1,
                           required=True)
    desc = forms.CharField(max_length=1024, required=False)
    body_type = forms.CharField(max_length=32)
    base_url = forms.CharField(max_length=128)
    up_func = forms.CharField(max_length=128)
    down_func = forms.CharField(max_length=128)
    method = forms.CharField(max_length=32)
    body_form_data = forms.CharField(required=False)
    body_json = forms.CharField(required=False)
    url_param = forms.CharField(required=False)
    url = forms.CharField(max_length=256, required=True)
    skip = forms.CharField(max_length=256, required=False)
    extract = forms.CharField(max_length=2048)
    validate = forms.CharField(max_length=2048)
    header = forms.CharField(max_length=2048)
    module = forms.CharField(max_length=128)
    module_id = forms.IntegerField(required=True)
    project_id = forms.IntegerField(required=True)


