# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('devotionals.views',
    url(r'^(?P<day>\d+)/(?P<month>\d+)/$',
        'get_devotional',
        name='dev'),
    url(r'^num_words/(?P<day>\d+)/(?P<month>\d+)/$',
        'get_devotional_num_words',
        name='num_words'),
)
