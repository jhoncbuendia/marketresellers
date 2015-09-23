from django.shortcuts import render
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from registro.models import  Perfil, Tienda, Cliente
from django.contrib.auth import authenticate, login as login_django
from django.shortcuts import redirect
from registro.serializers import ClienteSerializer
import json
from bson import json_util
from django.core import serializers
from django.contrib.auth import logout
# Create your views here.

def registrar(request):
	return render(request, 'login/registrar.html')

def ingresar(request):
	return render(request, 'login/ingresar.html')

def crear(request):
	usuario = request.POST.get('usuario', ' ')
	password = request.POST.get('password', ' ')
	u = User.objects.filter(username = usuario)

	if len(u):
		return render(request, 'mensaje/index.html', {'mensaje': 'Ya existe un usuario registrado con este correo', 'url':'/login/registrar/', 'link': 'volver'})
	else:
		user = User.objects.create_user(usuario, '', password)
		tienda = Tienda()
		tienda.url = usuario
		tienda.save()
		perfil = Perfil()
		perfil.usuario = user
		perfil.tienda = tienda
		perfil.save()
		u = authenticate(username = usuario, password = password)
		login_django(request, u)
		return redirect('/tienda/incluir/producto/')
		#return render(request, 'mensaje/index.html', {'mensaje': 'Usuario creado con exito', 'url':''})
	
		
def autenticar(request):
	usuario = request.POST.get('usuario', ' ')
	password = request.POST.get('password', ' ')
	user = authenticate(username = usuario, password = password)

	if user is not None:
		if user.is_active:					
					
			login_django(request, user)				
			return redirect('/tienda/crear/')	
			
			
		else:
			return render(request, 'mensaje/index.html', {'mensaje': 'Este usuario se encuentra inactivo', 'url':'/login/ingresar/', 'link': 'volver'})
	else:
		return render(request, 'mensaje/index.html', {'mensaje': 'Usuario o password incorrectos', 'url':'/login/ingresar/', 'link': 'volver'})

	

def crear_cliente(request):
	usuario = request.POST.get('usuario', ' ')
	password = request.POST.get('password', ' ')
	return HttpResponse(usuario+password)
	u = User.objects.filter(username = usuario)

	if len(u):
		return render(request, 'mensaje/index.html', {'mensaje': 'Ya existe un usuario registrado con este correo', 'url':'/login/registrar/', 'link': 'volver'})
	else:
		user = User.objects.create_user(usuario, '', password)
		tienda = Tienda()
		tienda.url = usuario
		tienda.save()
		perfil = Perfil()
		perfil.usuario = user
		perfil.tienda = tienda
		perfil.save()
		u = authenticate(username = usuario, password = password)
		login_django(request, u)
		return redirect('/tienda/crear/')

def autenticar_cliente(request):
	usuario = request.GET.get('usuario', ' ')
	password = request.GET.get('password', ' ')
	user = authenticate(username = usuario, password = password)
	response_data = {}	
	if user is not None:
		if user.is_active:					
			cliente = Cliente.objects.filter(usuario = user)
			if len(cliente):
				c = ClienteSerializer(cliente, many = True)
				response_data['codigo'] = 200
				response_data['cliente'] = c.data
				login_django(request, user)		
				return HttpResponse(json.dumps(c.data, default=json_util.default), content_type="application/json")	
					
			
			
			
		else:
			return render(request, 'mensaje/index.html', {'mensaje': 'Este usuario se encuentra inactivo', 'url':'/login/ingresar/', 'link': 'volver'})
	else:
		response_data['codigo'] = 404
		return HttpResponse(json.dumps(response_data), content_type="application/json")	




def salir(request):
	logout(request)
	return redirect('/')
