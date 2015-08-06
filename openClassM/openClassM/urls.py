"""openclassm URL Configuration

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
from django.conf.urls import patterns,include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accueil/$', 'tutoriels.views.accueil_dir'),
    url(r'^accueiltutoriels/$', 'tutoriels.views.categorie_dir'),
    url(r'^tutoriels/(?P<categorie_id>\d+)/$', 'tutoriels.views.article_dir'),
    url(r'^tutoriels/(?P<categorie_id>\d+)/(?P<article_id>\d+)/$', 'tutoriels.views.article_read'),
    url(r'^accueilforum/$', 'forum.views.forum_dir'),
    url(r'^forum/(?P<forum_id>\d+)/$', 'forum.views.thread_dir'),
    url(r'^thread/(?P<thread_id>\d+)/$', 'forum.views.post_dir'),
    url(r'^contact/$', 'contact.views.contact'),
    )
