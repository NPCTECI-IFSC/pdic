# encoding: utf-8
from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^tarefa/new/$', TarefaForm.as_view(), name='create-tarefa'),
    url(r'^rota/new/$', RotaForm.as_view(), name='create-rota'),
    url(r'^visao/new/$', VisaoForm.as_view(), name='create-visao'),
    url(r'^fator/new/$', FatorForm.as_view(), name='create-fator'),
    url(r'^responsavel/new/$', ResponsavelForm.as_view(), name='create-resp'),
    url(r'^tema/new/$', TemaForm.as_view(), name='create-tema'),
    url(r'^acao/new/$', AcaoForm.as_view(), name='create-acao')
]
