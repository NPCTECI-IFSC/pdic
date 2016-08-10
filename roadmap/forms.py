# encoding: utf-8
from django import forms
from roadmap.models import *
from util import fix_fields


class TarefaForm(forms.ModelForm):

    visao = forms.ModelChoiceField(
        queryset=Visao.objects.filter(ativa=True),
        label=u'Visão',
        required=False
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
        fix_fields(self.fields)

    def save(self, commit=True):
        acao = Acao.objects.get(id=self.data.get('acao'))
        self.instance.acao = acao
        return super(TarefaForm, self).save()


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

    def __init__(self, *args, **kwargs):
        super(AcaoForm, self).__init__(*args, **kwargs)
        fix_fields(self.fields)
