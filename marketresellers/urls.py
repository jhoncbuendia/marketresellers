from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'referidos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'main.views.index'),
    url(r'^producto/$', 'main.views.producto'),

   


    


    url(r'^perfil/$', 'perfil.views.index'),


    
    url(r'^referido/(?P<usuario>[0-9]+)/(?P<tienda>[0-9]+)/', 'perfil.views.redirect_tienda'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^social/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^service/', include('registro.urls')),
    url(r'^nuevo/cliente/', 'perfil.views.nuevo_cliente'),


    #urls tienda
    url(r'^store/(?P<usuario>.+)/$', 'tienda.views.ver_tienda'),
    url(r'^tienda/crear/$', 'tienda.views.crear_tienda'),
    url(r'^tienda/visualizar/$', 'tienda.views.visualizar_tienda'),
    url(r'^tienda/productos/incluidos/$', 'tienda.views.productos_incluidos_categoria'),



     url(r'^login/', include('login.urls')),


)


