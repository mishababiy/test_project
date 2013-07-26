# coding: utf-8

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
import views



admin.autodiscover()


urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ulogin/',  include('django_ulogin.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page':'/'}, name='logout'),
    url(r'^media/(?P<path>.*)', 'django.views.static.serve', kwargs={'document_root': settings.MEDIA_ROOT}),
    url(r'^ajax_comment/(?P<id_lesson>\d{1,5})$',views.ajax_comment),
    url(r'^view_lesson/(?P<id_lesson>\d{1,5})/$',views.view_lesson),
]

