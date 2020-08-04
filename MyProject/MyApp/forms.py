from django import forms

class NameForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='last Name', max_length=100)
    email = forms.CharField(label='email address', max_length=100)
    age = forms.IntegerField(label='Age', max_value=100)
