# encoding: utf-8
from __future__ import unicode_literals

from django.conf.urls import url, include
from django.contrib import admin
from pdic.api.urls import router
from roadmap.views import Index

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^pdic/', include('roadmap.urls', namespace='pdic'))
]
