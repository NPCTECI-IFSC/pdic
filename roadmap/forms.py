# encoding: utf-8
from django import forms
from roadmap.models import *


class TarefaForm(forms.ModelForm):

    visao = forms.ModelChoiceField(
        queryset=Visao.objects.filter(ativa=True)
    )
    fator = forms.ModelChoiceField(
        queryset=Fator.objects.filter(ativo=True)
    )

    class Meta:
        model = Tarefa
        fields = (
            'status',
            'data_inicio',
            'data_fim',
            'porcentagem',
            'descricao',
            'visao',
            'fator',
            'acao',
            'responsaveis',
            'ativa'
        )
