# encoding: utf-8
from __future__ import unicode_literals

from accounts.models import *
from django import forms
from roadmap.models import *
from util.forms import fix_fields


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
            'responsavel',
            'ativa',
            'visao'
        )

    def __init__(self, *args, **kwargs):
        super(TarefaForm, self).__init__(*args, **kwargs)
        fix_fields(self.fields)

    def clean(self):
        super(TarefaForm, self).clean()
        data_inicio = self.cleaned_data.get('data_inicio')
        data_fim = self.cleaned_data.get('data_fim')
        if (data_fim and data_inicio) and data_fim < data_inicio:
            raise forms.ValidationError(u'A data final não pode preceder a data inicial.')
        if not self.data.get('acao'):
            raise forms.ValidationError(u'A tarefa deve estar associada à uma ação.')
        return self.cleaned_data

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
        fields = ('nome', 'ativa', 'visao')

    def __init__(self, *args, **kwargs):
        super(FatorForm, self).__init__(*args, **kwargs)
        fix_fields(self.fields)


class ResponsavelForm(forms.ModelForm):

    class Meta:
        model = Responsavel
        fields = ('nome', 'ativa')

    def __init__(self, *args, **kwargs):
        super(ResponsavelForm, self).__init__(*args, **kwargs)
        fix_fields(self.fields)


class TemaForm(forms.ModelForm):

    class Meta:
        model = Tema
        fields = ('descricao', 'assunto', 'ativa', 'prioridade')

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

    def clean(self):
        super(AcaoForm, self).clean()
        data_inicio = self.cleaned_data.get('data_inicio')
        data_fim = self.cleaned_data.get('data_fim')
        if (data_fim and data_inicio) and data_fim < data_inicio:
            raise forms.ValidationError(u'A data final não pode preceder a data inicial.')
        return self.cleaned_data


class TendenciaForm(forms.ModelForm):

    class Meta:
        model = Tendencia
        fields = (
            'descricao',
            'rota',
            'ativa'
        )

    def __init__(self, *args, **kwargs):
        super(TendenciaForm, self).__init__(*args, **kwargs)
        fix_fields(self.fields)


class ConhecimentoForm(forms.ModelForm):

    rota = forms.ModelChoiceField(
        queryset=Rota.objects.filter(ativa=True),
        label=u'Rota',
        required=False
    )

    class Meta:
        model = Conhecimento
        fields = (
            'descricao',
            'ativa'
        )

    def __init__(self, *args, **kwargs):
        super(ConhecimentoForm, self).__init__(*args, **kwargs)
        fix_fields(self.fields)

    def clean(self):
        super(ConhecimentoForm, self).clean()
        if not self.data.get('tendencia'):
            raise forms.ValidationError(
                u'O conhecimento chave deve estar associado à uma tendência setorial.'
            )
        return self.cleaned_data

    def save(self, commit=True):
        tendencia = Tendencia.objects.get(id=self.data.get('tendencia'))
        self.instance.tendencia = tendencia
        return super(ConhecimentoForm, self).save()
