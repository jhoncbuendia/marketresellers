from rest_framework.serializers import ModelSerializer
from registro.models import Tienda, Perfil, Cliente, Producto, Cliente

class TiendaSerializer(ModelSerializer):
    class Meta:
        model = Tienda
        field = ('id', 'productos' )


class PerfilSerializer(ModelSerializer):
    class Meta:
        model = Perfil
        field = ('id', 'usuario', 'Titular_cuenta_bancaria', 'banco', 'numero_cuenta', 'pais', 'ciudad')

     


class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        field = ('id', 'nombre', 'descripcion', 'categoria', 'valor', 'peso')

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        field = ( 'pais', 'ciudad', 'direccion', 'telefono', 'fecha_creacion')