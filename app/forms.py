from django import forms


class mainForm(forms.Form):
    name = forms.CharField(label='Name', max_length=20)
    location = forms.CharField(label='Location', max_length=30)