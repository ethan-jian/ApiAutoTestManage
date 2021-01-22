from django import forms


class ProjectForm(forms.Form):
    user_id = forms.IntegerField(required=True)
    name = forms.CharField(max_length=64,
                           min_length=1,
                           required=True)
    test_environment = forms.CharField(max_length=1024, required=False)
    dev_environment = forms.CharField(max_length=1024, required=False)
    online_environment = forms.CharField(max_length=1024, required=False)
    bak_environment = forms.CharField(max_length=1024, required=False)
    environment_type = forms.CharField(max_length=1, required=True)
    principal = forms.CharField(max_length=16, required=False)
    variables = forms.CharField(max_length=2048, required=False)
    headers = forms.CharField(max_length=1024, required=False)
    func_file = forms.CharField(max_length=64, required=False)
    desc = forms.CharField(max_length=1024, required=False)


