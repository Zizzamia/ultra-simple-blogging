# -*- coding: utf-8 -*-
"""
urls.py
~~~~~~

"""
from django.conf.urls.defaults import *
from django.conf import settings
from core import views

urlpatterns = patterns(
    'core.views',
    (r'^$', 'home'),
    (r'create_post', 'create_post'),
    (r'^edit_post/(?P<post_id>[-\w]+)/$', 'edit_post'),
    (r'^delete_post/(?P<post_id>[-\w]+)/$', 'delete_post'),
    (r'^post/(?P<post_id>[-\w]+)/$', 'read_post'),
    (r'^__exception_test__/$', views.exception_test, {}),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^500/$', 'django.views.generic.simple.direct_to_template', {'template': '500.html'}),
        url(r'^404/$', 'django.views.generic.simple.direct_to_template', {'template': '404.html'}),
        )
