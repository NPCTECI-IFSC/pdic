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


class TendenciaSerializer(serializers.ModelSerializer):

    rota = RotaSerializer()

    class Meta:
        model = Tendencia
        fields = (
            'id',
            'descricao',
            'rota',
            'ativa'
        )


class ConhecimentoSerializer(serializers.ModelSerializer):

    tendencia = TendenciaSerializer()

    class Meta:
        model = Conhecimento
        fields = (
            'id',
            'descricao',
            'tendencia',
            'ativa'
        )


# PARTE ESPECÍFICA PARA RELATÓRIOS
class Relatorio1ConhecimentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conhecimento
        fields = ('id', 'descricao', 'ativa')


class Relatorio1TendenciaSerializer(serializers.ModelSerializer):

    conhecimentos = Relatorio1ConhecimentoSerializer(many=True)

    class Meta:
        model = Tendencia
        fields = ('id', 'descricao', 'ativa', 'conhecimentos')


class Relatorio1Serializer(serializers.ModelSerializer):

    tendencias = Relatorio1TendenciaSerializer(many=True)

    class Meta:
        model = Rota
        fields = ('id', 'nome', 'ativa', 'tendencias')
