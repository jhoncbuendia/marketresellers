from django.shortcuts import render
from registro.models import Categoria, Perfil, Tienda, Producto
from django.http.response import HttpResponse
import json
from registro.serializers import ProductoSerializer
from rest_framework.response import Response
# Create your views here.

def crear_tienda(request):
	categorias = Categoria.objects.all()
	usuario = request.user
	perfil = Perfil.objects.filter( usuario = usuario)
	
	
	return render(request, 'tienda/crear.html', {'categorias': categorias, 'tienda': perfil[0].tienda, 'perfil': perfil[0] })
	



def visualizar_tienda(request):
	categorias = Categoria.objects.all()
	usuario = request.user
	perfil = Perfil.objects.filter( usuario = usuario)
	if(len(perfil)):
		return render(request, 'tienda/visualizar.html', {'categorias': categorias, 'tienda': perfil[0].tienda})


def productos_incluidos_categoria(request):
	tienda = request.GET.get('tienda', 0)
	categoria = request.GET.get('categoria', 0)

	productos = Producto.objects.filter(categoria__id = categoria, tienda__id = tienda)
	response_data = {}
	response_data['result'] = 'failed'
	response_data['message'] = 'You messed up'
	serializer = ProductoSerializer(productos, many = True)
	#return Response(serializer.data)
	return HttpResponse(json.dumps(serializer.data), content_type="application/json")

def ver_tienda(request, usuario):
	categorias = Categoria.objects.all()
	tienda = Tienda.objects.filter(url = usuario)
	if(len(tienda)):
		return render(request, 'tienda/tienda.html', {'categorias': categorias, 'tienda': tienda[0] })
	else:
		return HttpResponse("tienda no encontrada")	