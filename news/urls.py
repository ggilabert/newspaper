from django.conf.urls import patterns, url
from django.contrib import admin

urlpatterns = patterns('news.views',
    url(r'^$', 'news_list', name='news_list'),

)


