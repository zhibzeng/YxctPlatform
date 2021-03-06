"""YxctPlatform URL Configuration

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

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # Examples:
    url(r'^$', 'MainApp.views.index', name='homepage'),
    url(r'^add/$', 'MainApp.views.add', name='sum'),
    # 采用 /add/3/4/ 这样的传值方式，请求参数在函数中体现
    url(r'^add/(\d+)/(\d+)/$', 'MainApp.views.add2', name='add2'),
    url(r'^login/$',  'MainApp.views.login', name='login'),
    url(r'^logout/$', 'MainApp.views.logout', name='logout'),
]
