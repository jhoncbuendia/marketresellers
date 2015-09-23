from django.conf.urls import patterns, include, url
from django.contrib.redirects import models
from registro.views import TiendaList, TiendaDetail, PerfilList, PerfilDetail, ClienteList, ClienteDetail, ProductoList
    # Examples:
    # url(r'^$', 'wiiaccessapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    #urls OstApiK
urlpatterns = patterns('',
	
    url(r'^tienda/list/', TiendaList),
    url(r'^tienda/detail/(?P<pk>[0-9]+)/', TiendaDetail),


    url(r'^perfil/list/', PerfilList),
    url(r'^perfil/detail/(?P<pk>[0-9]+)/', PerfilDetail),

    url(r'^cliente/list/', ClienteList),
    url(r'^cliente/detail/(?P<pk>[0-9]+)/', ClienteDetail),


    url(r'^producto/list/(?P<categoria>[0-9]+)/', ProductoList),


    
)