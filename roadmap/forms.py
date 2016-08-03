# encoding: utf-8
from django import forms
from roadmap.models import *

def fix_fields(fields):
    for field in fields.values():
        field.widget.attrs.update({
            'class': 'form-control'
        })


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
        widgets = {
            'data_inicio': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),
            'data_fim': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super(TarefaForm, self).__init__(*args, **kwargs)
        fix_fields(self.fields)


class RotaForm(forms.ModelForm):

    class Meta:
        model = Rota
        fields = ('nome', 'ativa')

    def __init__(self, *args, **kwargs):
        super(RotaForm, self).__init__(*args, **kwargs)
        fix_fields(self.fields)


class VisaoForm(forms.ModelForm):

    class Meta:
        model = Visao
        fields = ('descricao', 'rota', 'ativa', 'tipo')

    def __init__(self, *args, **kwargs):
        super(VisaoForm, self).__init__(*args, **kwargs)
        fix_fields(self.fields)


class FatorForm(forms.ModelForm):

    class Meta:
        model = Fator
        fields = ('nome', 'ativo', 'visao')

    def __init__(self, *args, **kwargs):
        super(FatorForm, self).__init__(*args, **kwargs)
        fix_fields(self.fields)


class ResponsavelForm(forms.ModelForm):

    class Meta:
        model = Responsavel
        fields = ('nome', 'ativo')

    def __init__(self, *args, **kwargs):
        super(ResponsavelForm, self).__init__(*args, **kwargs)
        fix_fields(self.fields)


class TemaForm(forms.ModelForm):

    class Meta:
        model = Tema
        fields = ('descricao', 'assunto', 'ativo', 'prioridade')

    def __init__(self, *args, **kwargs):
        super(TemaForm, self).__init__(*args, **kwargs)
        fix_fields(self.fields)


class AcaoForm(forms.ModelForm):

    class Meta:
        model = Acao
        fields = (
            'descricao',
            'motivo',
            'valor',
            'data_inicio',
            'data_fim',
            'local',
            'ativa',
            'tipo',
            'responsavel',
            'numero',
            'fator',
            'temas'
        )
        widgets = {
            'data_inicio': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),
            'data_fim': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super(AcaoForm, self).__init__(*args, **kwargs)
        fix_fields(self.fields)
