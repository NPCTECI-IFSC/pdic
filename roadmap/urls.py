# encoding: utf-8
from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^tarefas/$', TarefaList.as_view(), name='list-tarefas'),
    url(r'^tarefas/new/$', TarefaCreate.as_view(), name='create-tarefa'),
    url(r'^tarefas/edit/(?P<pk>[0-9]+)/$', TarefaEdit.as_view(), name='edit-tarefa'),
    url(r'^tarefas/delete/(?P<pk>[0-9]+)/$', TarefaDelete.as_view(), name='delete-tarefa'),
    url(r'^rotas/$', RotaList.as_view(), name='list-rotas'),
    url(r'^rotas/new/$', RotaCreate.as_view(), name='create-rota'),
    url(r'^rotas/edit/(?P<pk>[0-9]+)/$', RotaEdit.as_view(), name='edit-rota'),
    url(r'^visoes/$', VisaoList.as_view(), name='list-visoes'),
    url(r'^visoes/new/$', VisaoCreate.as_view(), name='create-visao'),
    url(r'^visoes/edit/(?P<pk>[0-9]+)/$', VisaoEdit.as_view(), name='edit-visao'),
    url(r'^fatores/$', FatorList.as_view(), name='list-fatores'),
    url(r'^fatores/new/$', FatorCreate.as_view(), name='create-fator'),
    url(r'^fatores/edit/(?P<pk>[0-9]+)/$', FatorEdit.as_view(), name='edit-fator'),
    url(r'^responsaveis/$', ResponsavelList.as_view(), name='list-responsaveis'),
    url(r'^responsaveis/new/$', ResponsavelCreate.as_view(), name='create-resp'),
    url(r'^responsaveis/edit/(?P<pk>[0-9]+)/$', ResponsavelEdit.as_view(), name='edit-responsavel'),
    url(r'^temas/$', TemaList.as_view(), name='list-temas'),
    url(r'^temas/new/$', TemaCreate.as_view(), name='create-tema'),
    url(r'^temas/edit/(?P<pk>[0-9]+)/$', TemaEdit.as_view(), name='edit-tema'),
    url(r'^acoes/$', AcaoList.as_view(), name='list-acoes'),
    url(r'^acoes/new/$', AcaoCreate.as_view(), name='create-acao'),
    url(r'^acoes/edit/(?P<pk>[0-9]+)/$', AcaoEdit.as_view(), name='edit-acao')
]
