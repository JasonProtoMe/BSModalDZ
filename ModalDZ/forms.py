from django import forms

import datetime

class InfoForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    date = forms.DateField(initial=datetime.date.today)
    checkbox = forms.BooleanField(required=False)
