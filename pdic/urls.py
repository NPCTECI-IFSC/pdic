# encoding: utf-8
from django.conf.urls import url, include
from django.contrib import admin

from pdic.api.urls import router
from roadmap.views import Index

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^pdic/', include('roadmap.urls', namespace='roadmap'))
]