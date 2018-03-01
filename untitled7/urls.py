"""untitled7 URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from app1 import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login',views.login),
    url(r'^index',views.index),
    url(r'hostlist',views.hostlist),
    url(r'addhost',views.addhost),
    url(r'^delhost-(\d+).html',views.delhost),
    url(r'^edithost-*(\d+)*.html',views.edithost),
    url(r'^console',views.console),
    url(r'^shell-*(\d+)*.html',views.host_connect),
    url(r'^test',views.celery11),
    url(r'^ansible',views.run_ansible),
    url(r'^ajax.html',views.ajax_test),
    url(r'^ajax_submit',views.ajax_submit),
    url(r'^upload',views.upload),
]
