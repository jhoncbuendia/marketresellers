from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tienda(models.Model):
	url = models.CharField(max_length=50,  blank = True, null = True)	
	productos =  models.ManyToManyField('Producto')
	def __unicode__(self):
		return self.url

class Venta(models.Model):
	fuente = models.CharField(max_length=50)
	valor = models.CharField(max_length=50)
	cliente = models.CharField(max_length=50)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	confirmacion_de_pago = models.BooleanField(default = False)
	vendedor =  models.ForeignKey('Perfil')

	def __unicode__(self):
		return self.fuente

class Perfil(models.Model):
	usuario = models.ForeignKey(User, null = True,  blank = True)
	tienda = models.ForeignKey('Tienda',  blank = True, null = True)
	Titular_cuenta_bancaria = models.CharField(max_length=100, blank = True, null = True)
	banco = models.CharField(max_length=50, blank = True, null = True)
	numero_cuenta = models.CharField(max_length=50, blank = True, null = True)
	pais = models.CharField(max_length=50, blank = True, null = True)
	ciudad = models.CharField(max_length=50, blank = True, null = True)

	def __unicode__(self):
		return str(self.usuario)

class Cliente(models.Model):
	usuario = models.ForeignKey(User, null = True,  blank = True)	
	pais = models.CharField(max_length=100, blank = True, null = True)
	ciudad = models.CharField(max_length=100, blank = True, null = True)
	direccion = models.CharField(max_length=100, blank = True, null = True)
	telefono = models.CharField(max_length=100, blank = True, null = True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)	
	
	def __unicode__(self):
		return str(self.usuario)

class Categoria(models.Model):
	nombre = models.CharField(max_length=50, blank = True, null = True)
	

	def __unicode__(self):
		return str(self.nombre)



class Producto(models.Model):
	nombre = models.CharField(max_length=50, blank = True, null = True)
	descripcion = models.TextField(max_length=500, blank = True, null = True)
	categoria = models.ForeignKey('Categoria')
	valor = models.IntegerField(max_length=20, blank = True, null = True)
	peso = models.IntegerField(max_length=20, blank = True, null = True)
	estado = models.BooleanField(default = False)
	privado = models.BooleanField(default = False)
	def __unicode__(self):
		return str(self.nombre)


class Inventario(models.Model):
	
	
	categoria = models.ForeignKey('Producto')
	existencia = models.IntegerField(max_length=10, blank = True, null = True)	

	def __unicode__(self):
		return str(self.nombre)



