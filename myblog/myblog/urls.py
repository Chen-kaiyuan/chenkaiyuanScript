from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',


    url(r'^admin/', include(admin.site.urls)), #admin
    url(r'^$', 'article.views.home', name='home'), #home
    url(r'^(?P<id>\d+)/$', 'article.views.detail', name='detail'), # atctle
    url(r'^archives/$', 'article.views.archives', name = 'archives'),

)
