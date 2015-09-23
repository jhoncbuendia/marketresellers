from django.shortcuts import render
from django.http import HttpResponse
from registro.models import Categoria
# Create your views here.

def index(request):
	return render(request, 'layouts/index.html')

def producto(request):
	return render(request, 'layouts/producto.html')


def crear_tienda(request):
	categorias = Categoria.objects.all()
	return render(request, 'tienda/crear.html', {'categorias': categorias})

