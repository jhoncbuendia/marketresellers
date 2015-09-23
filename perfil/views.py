from django.shortcuts import render
from django.http import HttpResponse
from registro.models import Tienda, Perfil, Cliente
# Create your views here.

def index(request):
	if request.user.is_active:
		tiendas = Tienda.objects.all()
		perfil = Perfil.objects.filter( usuario = request.user)
		if len(perfil):
			return render(request, 'perfil/index.html', {'usuario': request.user, 'tiendas': tiendas })
		else:
			perfil = Perfil()
			perfil.usuario = request.user
			perfil.save()
			return render(request, 'perfil/index.html', {'usuario': request.user, 'tiendas': tiendas })
	else:
		return render(request, 'error/index.html', { 'mensaje' : 'Por favor ingrese primero a la aplicacion.'})


def redirect_tienda(request, usuario, tienda):
	vendedora = Perfil.objects.filter( usuario__id = usuario )
	tienda = Tienda.objects.filter( id = tienda)
	#return HttpResponse(vendedora)
	return render(request, 'perfil/referido.html', {'vendedora': vendedora[0].usuario , 'tienda': tienda[0]})
	return HttpResponse("usuario: "+ usuario + " tienda: "+tienda)


def nuevo_cliente(request):

	correo = request.GET.get('correo')
	vendedora = request.GET.get('vendedora')
	tienda =  request.GET.get('tienda')
	
	#return HttpResponse("Creando cliene y redireccionando a la tienda: "+tienda)
	perfil = Perfil.objects.filter( usuario__id = vendedora)
	#return HttpResponse(perfil[0])

	cliente =  Cliente()
	cliente.tienda =  tienda
	cliente.correo = correo
	cliente.vendedor = perfil[0]
	cliente.save()
	return HttpResponse("data"+str(correo)+str(vendedora)+str(tienda))
