# encoding: utf-8
from __future__ import unicode_literals

from pdic.api.filters import *
from pdic.api.serializers import *
from rest_framework.filters import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.filter(ativa=True)
    serializer_class = UsuarioSerializer


class RotaViewSet(ModelViewSet):
    queryset = Rota.objects.filter(ativa=True)
    serializer_class = RotaSerializer


class VisaoViewSet(ModelViewSet):
    queryset = Visao.objects.filter(ativa=True)
    serializer_class = VisaoSerializer


class FatorViewSet(ModelViewSet):
    queryset = Fator.objects.filter(ativa=True)
    serializer_class = FatorSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = FatorFilter


class AcaoViewSet(ModelViewSet):
    queryset = Acao.objects.filter(ativa=True)
    serializer_class = AcaoSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = AcaoFilter


class ResponsavelViewSet(ModelViewSet):
    queryset = Responsavel.objects.filter(ativa=True)
    serializer_class = ResponsavelSerializer


class TemaViewSet(ModelViewSet):
    queryset = Tema.objects.filter(ativa=True)
    serializer_class = TemaSerializer


class TarefaViewSet(ModelViewSet):
    queryset = Tarefa.objects.filter(ativa=True)
    serializer_class = TarefaSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = TarefaFilter
