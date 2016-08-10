# encoding: utf-8
from .models import Usuario
from django import forms
from util import fix_fields


class UsuarioForm(forms.ModelForm):
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'password', 'regiao', 'ativo')

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        fix_fields(self.fields)

    def save(self, commit=True):
        password = self.cleaned_data.get('password')
        self.instance.set_password(password)
        super(UsuarioForm, self).save()


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        fix_fields(self.fields)
