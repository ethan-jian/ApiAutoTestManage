from django import forms


class ModuleForm(forms.Form):
    name = forms.CharField(max_length=64,
                           min_length=1,
                           required=True)
    project_id = forms.IntegerField(required=True)
    desc = forms.CharField(max_length=1024, required=False)

