from django import forms


class CaseForm(forms.Form):
    name = forms.CharField(max_length=128,
                           min_length=1,
                           required=True)
    desc = forms.CharField(max_length=256, required=False)
    case_set_id = forms.IntegerField(required=True)
    project_id = forms.IntegerField(required=True)


