from django import forms


class DataForm(forms.Form):
    number = forms.DecimalField(label='')#, min_value=1, max_value=3999)