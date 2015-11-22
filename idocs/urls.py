"""iDocs URL Configuration

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

from idocsapp.views import index, proposta, empresa, download, produtos
from idocsapp.views import detail
from idocsapp.views import results
from idocsapp.views import vote

urlpatterns = [
    url(r'^$', index),
    url(r'^proposta/$', proposta, name="proposta"),
    url(r'^empresa/$', empresa, name="empresa"),
    url(r'^download/$', download, name="download"),
    url(r'^produtos/$', produtos, name="produtos"),

    url(r'^(?P<question_id>[0-9]+)/$', detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', vote, name='vote'),

    url(r'^admin/', include(admin.site.urls)),

]
