# encoding: utf-8
from django import forms
from roadmap.models import *


class TarefaForm(forms.ModelForm):

    visao = forms.ModelChoiceField(
        queryset=Visao.objects.filter(ativa=True),
        label=u'Visão'
    )

    class Meta:
        model = Tarefa
        fields = (
            'status',
            'data_inicio',
            'data_fim',
            'porcentagem',
            'descricao',
            'responsaveis',
            'ativa',
            'visao'
        )

    def __init__(self, *args, **kwargs):
        super(TarefaForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })
