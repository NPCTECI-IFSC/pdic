# encoding: utf-8
from .models import Usuario
from django import forms


class UsuarioForm(forms.ModelForm):

    password = forms.CharField(max_length=128, widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'password', 'regiao', 'ativo')
