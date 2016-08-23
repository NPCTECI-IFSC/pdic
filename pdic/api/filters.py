# encoding: utf-8
from __future__ import unicode_literals

import django_filters
from roadmap.models import *


class TarefaFilter(django_filters.FilterSet):

    class Meta:
        model = Tarefa
        fields = {
            'acao': ['exact']
        }


class FatorFilter(django_filters.FilterSet):

    class Meta:
        model = Fator
        fields = {
            'visao': ['exact']
        }


class AcaoFilter(django_filters.FilterSet):

    class Meta:
        model = Acao
        fields = {
            'fator': ['exact']
        }


class TendenciaFilter(django_filters.FilterSet):

    class Meta:
        model = Tendencia
        fields = {
            'rota': ['exact']
        }
