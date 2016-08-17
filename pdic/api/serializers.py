# encoding: utf-8
from __future__ import unicode_literals

from accounts.models import Usuario
from rest_framework import serializers
from roadmap.models import *


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'email', 'regiao', 'ativa')


class RotaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rota
        fields = ('id', 'nome', 'ativa')


class VisaoSerializer(serializers.ModelSerializer):

    rota = RotaSerializer()

    class Meta:
        model = Visao
        fields = ('id', 'descricao', 'rota', 'ativa', 'tipo')


class FatorSerializer(serializers.ModelSerializer):

    visao = VisaoSerializer()

    class Meta:
        model = Fator
        fields = ('id', 'nome', 'ativa', 'visao')


class ResponsavelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Responsavel
        fields = ('id', 'nome', 'ativa')


class TemaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tema
        fields = ('id', 'descricao', 'assunto', 'ativa', 'prioridade')


class AcaoSerializer(serializers.ModelSerializer):

    fator = FatorSerializer()
    temas = TemaSerializer(many=True)

    class Meta:
        model = Acao
        fields = (
            'id',
            'descricao',
            'motivo',
            'valor',
            'data_inicio',
            'data_fim',
            'local',
            'ativa',
            'tipo',
            'numero',
            'fator',
            'temas'
        )


class TarefaSerializer(serializers.ModelSerializer):

    acao = AcaoSerializer()
    responsavel = UsuarioSerializer()

    class Meta:
        model = Tarefa
        fields = (
            'id',
            'status',
            'data_inicio',
            'data_fim',
            'ativa',
            'porcentagem',
            'descricao',
            'acao',
            'responsavel'
        )
