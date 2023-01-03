"""my_django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from hello.views import index
from hello.views import index2
from hello.views import templateChallengeIndex
from hello.views import articles
from hello.views import forms
from hello.views import postindex
from hello.views import update
from hello.views import delete

app_name = "hello"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', index, name='firsthello'),
    path('hello2/', index2, name='secondhello'),
    path('templatechallenge/', templateChallengeIndex, name="templatechallenge"),
    re_path('^articles/(?P<year>[0-9]{4})/$', articles, name='dynamicarticles'),
    path('forms/', forms, name='forms'),
    path('postindex/', postindex, name='postindex'),
    re_path(r'^update/(?P<id>[0-9]+)/$', update, name='update'),
    re_path(r'^delete/(?P<id>[0-9]+)/$', delete, name='delete'),
]
