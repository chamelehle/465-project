"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
import app.views
from django.contrib import admin
import django.contrib.auth.views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', app.views.home, name='home'),
    url(r'^$', app.views.comments, name='comments'),
    url(r'^event', app.views.events, name='events'),
    url(r'^map', app.views.map, name='map'),
    url(r'^fact', app.views.facts, name='facts'),
    url(r'^login', app.views.login, name='login'),
    url(r'^about', app.views.about, name='about'),
]
