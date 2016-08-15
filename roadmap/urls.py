# encoding: utf-8
from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from roadmap.views import *

urlpatterns = [
    url(r'^tarefas/$', TarefaList.as_view(), name='list-tarefas'),
    url(r'^tarefas/new/$', login_required(TarefaCreate.as_view()), name='create-tarefa'),
    url(
        r'^tarefas/edit/(?P<pk>[0-9]+)/$',
        login_required(TarefaEdit.as_view()),
        name='edit-tarefa'
    ),
    url(
        r'^tarefas/delete/(?P<pk>[0-9]+)/$',
        login_required(TarefaDelete.as_view()),
        name='delete-tarefa'
    ),
    url(r'^rotas/$', RotaList.as_view(), name='list-rotas'),
    url(r'^rotas/new/$', login_required(RotaCreate.as_view()), name='create-rota'),
    url(
        r'^rotas/edit/(?P<pk>[0-9]+)/$',
        login_required(RotaEdit.as_view()),
        name='edit-rota'
    ),
    url(
        r'^rotas/delete/(?P<pk>[0-9]+)/$',
        login_required(RotaDelete.as_view()),
        name='delete-rota'
    ),
    url(r'^visoes/$', VisaoList.as_view(), name='list-visoes'),
    url(r'^visoes/new/$', login_required(VisaoCreate.as_view()), name='create-visao'),
    url(
        r'^visoes/edit/(?P<pk>[0-9]+)/$',
        login_required(VisaoEdit.as_view()),
        name='edit-visao'
    ),
    url(
        r'^visoes/delete/(?P<pk>[0-9]+)/$',
        login_required(VisaoDelete.as_view()),
        name='delete-visao'
    ),
    url(r'^fatores/$', FatorList.as_view(), name='list-fatores'),
    url(r'^fatores/new/$', login_required(FatorCreate.as_view()), name='create-fator'),
    url(
        r'^fatores/edit/(?P<pk>[0-9]+)/$',
        login_required(FatorEdit.as_view()),
        name='edit-fator'
    ),
    url(
        r'^fatores/delete/(?P<pk>[0-9]+)/$',
        login_required(FatorDelete.as_view()),
        name='delete-fator'
    ),
    url(r'^responsaveis/$', ResponsavelList.as_view(), name='list-responsaveis'),
    url(
        r'^responsaveis/new/$',
        login_required(ResponsavelCreate.as_view()),
        name='create-responsavel'
    ),
    url(
        r'^responsaveis/edit/(?P<pk>[0-9]+)/$',
        login_required(ResponsavelEdit.as_view()),
        name='edit-responsavel'
    ),
    url(
        r'^responsaveis/delete/(?P<pk>[0-9]+)/$',
        login_required(ResponsavelDelete.as_view()),
        name='delete-responsavel'
    ),
    url(r'^temas/$', TemaList.as_view(), name='list-temas'),
    url(r'^temas/new/$', login_required(TemaCreate.as_view()), name='create-tema'),
    url(
        r'^temas/edit/(?P<pk>[0-9]+)/$',
        login_required(TemaEdit.as_view()),
        name='edit-tema'
    ),
    url(
        r'^temas/delete/(?P<pk>[0-9]+)/$',
        login_required(TemaDelete.as_view()),
        name='delete-tema'
    ),
    url(r'^acoes/$', AcaoList.as_view(), name='list-acoes'),
    url(r'^acoes/new/$', login_required(AcaoCreate.as_view()), name='create-acao'),
    url(
        r'^acoes/edit/(?P<pk>[0-9]+)/$',
        login_required(AcaoEdit.as_view()),
        name='edit-acao'
    ),
    url(
        r'^acoes/delete/(?P<pk>[0-9]+)/$',
        login_required(AcaoDelete.as_view()),
        name='delete-acao'
    ),
    url(r'^relatorio/acoes/$', Relatorio3.as_view(), name='r3'),
    url(r'^relatorio/tarefas/(?P<pk>[0-9]+)/$', Relatorio4.as_view(), name='r4')
]
