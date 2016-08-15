# encoding: utf-8
from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', logout_view, name='logout')
]
