"""se_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
import settings
urlpatterns = [
    # static(r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^$','set.views.homepage',name='index'),
    url(r'^parent.html/','set.views.parent',name='parent'),
    url(r'^homepage.html/','set.views.homepage',name='homepage'),
    url(r'^sonEvent.html/','set.views.sonEvent',name='sonEvent'),
    url(r'^test/','set.views.test',name='test'),
    url(r'^ajax_dict/','set.views.ajax_dict',name='ajax_dict'),
    url(r'^ajax_list/','set.views.ajax_list',name='ajax_list'),

    url(r'^getCommentnum/','set.views.getCommentnum',name='getCommentnum'),
    url(r'^getNavs/','set.views.getNavs',name='getNavs'),
    url(r'^getHomeNews/','set.views.getHomeNews',name='getHomeNews'),
    url(r'^getBannerAndCharts/','set.views.getBannerAndCharts',name='getBannerAndCharts'),
    url(r'^getNewssource/','set.views.getNewssource',name='getNewssource'),
    url(r'^getEmotion/','set.views.getEmotion',name='getEmotion'),
    url(r'^getKeywordAndComment/','set.views.getKeywordAndComment',name='getKeywordAndComment'),

    url(r'^admin/', include(admin.site.urls)),
]
