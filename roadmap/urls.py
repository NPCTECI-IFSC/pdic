# encoding: utf-8
from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^tarefas/$', TarefaList.as_view(), name='list-tarefas'),
    url(r'^tarefa/new/$', TarefaForm.as_view(), name='create-tarefa'),
    url(r'^rotas/$', RotaList.as_view(), name='list-rotas'),
    url(r'^rota/new/$', RotaForm.as_view(), name='create-rota'),
    url(r'^visoes/$', VisaoList.as_view(), name='list-visoes'),
    url(r'^visao/new/$', VisaoForm.as_view(), name='create-visao'),
    url(r'^fatores/$', FatorList.as_view(), name='list-fatores'),
    url(r'^fator/new/$', FatorForm.as_view(), name='create-fator'),
    url(r'^responsaveis/$', ResponsavelList.as_view(), name='list-responsaveis'),
    url(r'^responsavel/new/$', ResponsavelForm.as_view(), name='create-resp'),
    url(r'^temas/$', TemaList.as_view(), name='list-temas'),
    url(r'^tema/new/$', TemaForm.as_view(), name='create-tema'),
    url(r'^acoes/$', AcaoList.as_view(), name='list-acoes'),
    url(r'^acao/new/$', AcaoForm.as_view(), name='create-acao')
]
