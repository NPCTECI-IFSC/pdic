# encoding: utf-8
from __future__ import unicode_literals

from pdic.api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'rotas', RotaViewSet)
router.register(r'visoes', VisaoViewSet)
router.register(r'fatores', FatorViewSet)
router.register(r'acoes', AcaoViewSet)
router.register(r'responsaveis', ResponsavelViewSet)
router.register(r'temas', TemaViewSet)
router.register(r'tarefas', TarefaViewSet)
