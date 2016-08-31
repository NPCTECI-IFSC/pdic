# encoding: utf-8
from __future__ import unicode_literals

from accounts.views import *
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(
        r'^responsaveis/$',
        ResponsavelList.as_view(),
        name='list-responsaveis'
    ),
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
    )
]
