from django import forms


class CaseSetForm(forms.Form):
    name = forms.CharField(max_length=64,
                           min_length=1,
                           required=True)
    desc = forms.CharField(max_length=1024, required=False)
    project_id = forms.IntegerField(required=True)


