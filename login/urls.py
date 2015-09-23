from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'referidos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^registrar/$', 'login.views.registrar'),
    url(r'^ingresar/$', 'login.views.ingresar'),
    url(r'^crear/usuario/$', 'login.views.crear'),
    url(r'^crear/cliente/$', 'login.views.crear_cliente'),
    url(r'^autenticar/usuario/$', 'login.views.autenticar'),
    url(r'^autenticar/cliente/$', 'login.views.autenticar_cliente'),


    url(r'^salir/$', 'login.views.salir'),
    


)


