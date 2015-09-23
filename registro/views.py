from django.http.response import HttpResponse, Http404

from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
import json
from registro.serializers import TiendaSerializer, PerfilSerializer, ClienteSerializer, ProductoSerializer
from registro.models import Tienda, Perfil, Cliente, Producto

class TiendaList(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format = None):
        tienda = Tienda.objects.all()
        serializer = TiendaSerializer(tienda, many = True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request):
        serializer = TiendaSerializer(data = request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TiendaDetail(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Tienda.objects.get(pk=pk)
        except Tienda.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = TiendaSerializer(survey, data = request.DATA)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, pk, format=None):
        survey = self.get_object(pk)
        survey.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = TiendaSerializer(survey, data = request.DATA)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



TiendaList = TiendaList.as_view()
TiendaDetail  = TiendaDetail.as_view()






class PerfilList(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format = None):
        perfil = Perfil.objects.all()
        serializer = PerfilSerializer(perfil, many = True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request):
        serializer = PerfilSerializer(data = request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PerfilDetail(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Perfil.objects.get(usuario__id = pk)
        except Perfil.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = PerfilSerializer(survey, data = request.DATA)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, pk, format=None):
        survey = self.get_object(pk)
        survey.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = PerfilSerializer(survey, data = request.DATA)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



PerfilList = PerfilList.as_view()
PerfilDetail  = PerfilDetail.as_view()



class ClienteList(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, format = None):
        cliente = Cliente.objects.all()
        serializer = ClienteSerializer(cliente, many = True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request):
        serializer = ClienteSerializer(data = request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClienteDetail(APIView):
    #permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Cliente.objects.get( usuario_id = pk)
        except Cliente.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = ClienteSerializer(survey, data = request.DATA)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, pk, format=None):
        survey = self.get_object(pk)
        survey.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = ClienteSerializer(survey, data = request.DATA)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



ClienteList = ClienteList.as_view()
ClienteDetail  = ClienteDetail.as_view()



class ProductoList(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request, categoria, format = None):
        productos = Producto.objects.filter( categoria = categoria)
        serializer = ProductoSerializer(productos, many = True)
        return Response(serializer.data)

ProductoList = ProductoList.as_view()






    
