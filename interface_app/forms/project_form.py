from django import forms


class ProjectForm(forms.Form):
    user_id = forms.IntegerField(required=True)
    name = forms.CharField(max_length=64,
                           min_length=1,
                           required=True)
    host = forms.CharField(max_length=1024, required=False)
    host_two = forms.CharField(max_length=1024, required=False)
    host_three = forms.CharField(max_length=1024, required=False)
    host_four = forms.CharField(max_length=1024, required=False)
    environment_choice = forms.CharField(max_length=16)
    principal = forms.CharField(max_length=16, required=False)
    variables = forms.CharField(max_length=2048, required=False)
    headers = forms.CharField(max_length=1024, required=False)
    func_file = forms.CharField(max_length=64, required=False)


