# encoding: utf-8
from __future__ import unicode_literals

from accounts.models import Usuario
from django.db import models


STATUS_TAREFA = (
    (u'EA', u'Em andamento'),
    (u'F', u'Finalizada'),
    (u'NI', u'Não iniciada')
)

TIPOS = (
    (u'CP', u'Curto prazo'),
    (u'MP', u'Médio prazo'),
    (u'LP', u'Longo prazo')
)


class Rota(models.Model):
    id = models.AutoField(primary_key=True, db_column='id_rota')
    nome = models.CharField(
        verbose_name=u'nome',
        max_length=100,
        db_column='nome_rota'
    )
    ativa = models.BooleanField(
        verbose_name=u'Ativa',
        default=True,
        db_column='ativa_rota'
    )

    class Meta:
        db_table = 'tb_rota'
        verbose_name = u'Rota'
        verbose_name_plural = u'Rotas'

    def __str__(self):
        return self.nome


class Visao(models.Model):
    id = models.AutoField(primary_key=True, db_column='id_visao')
    descricao = models.TextField(
        verbose_name=u'Descrição',
        max_length=400,
        db_column='desc_visao'
    )
    rota = models.ForeignKey(
        Rota,
        verbose_name=u'Rota',
        db_column='tb_rota_id'
    )
    ativa = models.BooleanField(
        verbose_name=u'Ativa',
        default=True,
        db_column='ativa_visao'
    )
    tipo = models.CharField(
        verbose_name=u'Tipo',
        max_length=100,
        choices=TIPOS,
        db_column='tipo_visao'
    )

    class Meta:
        db_table = 'tb_visao'
        verbose_name = u'Visão'
        verbose_name_plural = u'Visões'

    def __str__(self):
        return '%s...' % self.descricao[:30]


class Fator(models.Model):
    id = models.AutoField(primary_key=True, db_column='id_fator')
    nome = models.CharField(
        verbose_name=u'Nome',
        max_length=100,
        db_column='nome_fator'
    )
    ativo = models.BooleanField(
        verbose_name=u'Ativo',
        default=True,
        db_column='ativa_fator'
    )
    visao = models.ForeignKey(
        Visao,
        verbose_name=u'Visão',
        db_column='tb_visao_id'
    )

    class Meta:
        db_table = 'tb_fator_critico_sucesso'
        verbose_name = u'Fator'
        verbose_name_plural = u'Fatores'

    def __str__(self):
        return self.nome


class Responsavel(models.Model):
    id = models.AutoField(primary_key=True, db_column='id_resp')
    nome = models.CharField(
        verbose_name=u'Nome',
        max_length=100,
        db_column='nome_resp'
    )
    ativo = models.BooleanField(
        verbose_name=u'Ativo',
        default=True,
        db_column='tb_responsavel'
    )

    class Meta:
        db_table = 'tb_responsavel'
        verbose_name = u'Responsável'
        verbose_name_plural = u'Responsáveis'

    def __str__(self):
        return self.nome


class Tema(models.Model):
    id = models.AutoField(primary_key=True, db_column='id_tema')
    descricao = models.TextField(
        verbose_name=u'Descrição',
        max_length=400,
        db_column='descricao_tema'
    )
    assunto = models.TextField(
        verbose_name=u'Assunto',
        max_length=400,
        db_column='assunto_tema'
    )
    ativo = models.BooleanField(
        verbose_name=u'Ativo',
        default=True,
        db_column='ativa_tema'
    )
    prioridade = models.IntegerField(
        verbose_name=u'Prioridade',
        db_column='prioridade_tema'
    )

    class Meta:
        db_table = 'tb_tema'
        verbose_name = u'Tema'
        verbose_name_plural = u'Temas'

    def __str__(self):
        return '%s...' % self.descricao[:30]


class Acao(models.Model):
    id = models.AutoField(primary_key=True, db_column='id_acao')
    descricao = models.TextField(
        verbose_name=u'Descrição',
        max_length=400,
        db_column='desc_acao'
    )
    motivo = models.CharField(
        verbose_name=u'Motivo',
        max_length=255,
        blank=True,
        null=True,
        db_column='motivo_acao'
    )
    valor = models.FloatField(
        verbose_name=u'Valor',
        blank=True,
        null=True,
        db_column='valor_acao'
    )
    data_inicio = models.DateField(
        verbose_name=u'Data de início',
        db_column='data_inicio_acao'
    )
    data_fim = models.DateField(
        verbose_name=u'Data final',
        db_column='data_fim_acao'
    )
    local = models.CharField(
        verbose_name=u'Local',
        blank=True,
        null=True,
        max_length=100,
        db_column='local_acao'
    )
    ativa = models.BooleanField(
        verbose_name=u'Ativa',
        default=True,
        db_column='ativa_acao'
    )
    tipo = models.CharField(
        verbose_name=u'Tipo',
        max_length=100,
        choices=TIPOS,
        db_column='tipo_acao'
    )
    responsavel = models.ForeignKey(
        Responsavel,
        verbose_name=u'Responsável',
        db_column='tb_responsavel_id'
    )
    numero = models.IntegerField(
        verbose_name=u'Número',
        db_column='numero_acao'
    )
    fator = models.ForeignKey(
        Fator,
        verbose_name=u'Fator',
        db_column='tb_fator_critico_sucesso_id'
    )
    temas = models.ManyToManyField(
        Tema,
        verbose_name=u'Temas',
        related_name='acoes',
        db_table='tb_acao_has_tb_tema'
    )

    class Meta:
        db_table = 'tb_acao'
        verbose_name = u'Ação'
        verbose_name_plural = u'Ações'

    def __str__(self):
        return '%s...' % self.descricao[:30]


class Tarefa(models.Model):
    id = models.AutoField(primary_key=True, db_column='id_tarefa')
    status = models.CharField(
        verbose_name=u'Status',
        max_length=45,
        choices=STATUS_TAREFA,
        db_column='status_tarefa'
    )
    data_inicio = models.DateField(
        verbose_name=u'Data de início',
        db_column='data_inicio_tarefa'
    )
    data_fim = models.DateField(
        verbose_name=u'Data final',
        db_column='data_fim_tarefa'
    )
    ativa = models.BooleanField(
        verbose_name=u'Ativa',
        default=True,
        db_column='ativa_tarefa'
    )
    porcentagem = models.FloatField(
        verbose_name=u'Porcentagem',
        db_column='porc_concluida_tarefa'
    )
    descricao = models.TextField(
        verbose_name=u'Descrição',
        max_length=400,
        db_column='desc_tarefa'
    )
    acao = models.ForeignKey(
        Acao,
        verbose_name=u'Ação',
        db_column='tb_acao_id'
    )
    responsaveis = models.ManyToManyField(
        Usuario,
        verbose_name=u'Responsáveis',
        related_name='tarefas',
        db_table='tb_tarefa_has_tb_responsavel'
    )

    class Meta:
        db_table = 'tb_tarefa'
        verbose_name = u'Tarefa'
        verbose_name_plural = u'Tarefas'

    def __str__(self):
        return '{} - {}%'.format(self.get_status_display(), self.porcentagem)