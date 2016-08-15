# encoding: utf-8
from django import forms
from django.contrib.auth import authenticate
from util.forms import fix_fields


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        fix_fields(self.fields)

    def clean(self):
        super(LoginForm, self).clean()
        username = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if (username and password) and not user:
            raise forms.ValidationError(u'Login ou senha inválidos')
        return self.cleaned_data
