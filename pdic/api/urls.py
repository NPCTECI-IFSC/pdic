# encoding: utf-8
from __future__ import unicode_literals

from pdic.api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'rotas', RotaViewSet, 'rotas')
router.register(r'visoes', VisaoViewSet)
router.register(r'fatores', FatorViewSet)
router.register(r'acoes', AcaoViewSet)
router.register(r'responsaveis', ResponsavelViewSet)
router.register(r'temas', TemaViewSet)
router.register(r'tarefas', TarefaViewSet)
router.register(r'tendencias', TendenciaViewSet, 'tendencias')
router.register(r'conhecimentos', ConhecimentoViewSet)
router.register(r'relatorio1', Relatorio1ViewSet, 'relatorio1')
router.register(r'relatorio2', Relatorio2ViewSet, 'relatorio2')
