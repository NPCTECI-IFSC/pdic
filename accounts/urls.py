# encoding: utf-8
from __future__ import unicode_literals

from accounts.views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', logout_view, name='logout')
]
