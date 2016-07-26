# encoding: utf-8
from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^tarefa/new/$', TarefaForm.as_view(), name='create-tarefa'),
]
