from django.contrib import admin
from registro.models import  Venta, Perfil, Cliente, Categoria, Producto, Tienda
# Register your models here.

admin.site.register(Venta)
admin.site.register(Tienda)
admin.site.register(Perfil)
admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Producto)