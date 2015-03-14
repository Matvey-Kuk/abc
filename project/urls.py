from django.conf.urls import patterns, include, url
from django.contrib import admin

from project import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^lkdsfgds435m56jkh543k25f3465756jkh545/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG}),
    url(r'^$', 'application.views.index', name='index'),

    url(r'^get-messages/$', 'application.views.get_messages'),
)
