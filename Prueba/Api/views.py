from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class Index(APIView):
    def get(self,request):
        return Response("Index")
class ColegiosList(APIView):
    def get(self,request):
        colegios = CustomUser.objects.all()
        data = CustomUserSerializer(colegios,many=True).data
        return Response(data)

class ColegioDetail(APIView):
    def get(self,request):
        usuario = request.GET.get('usuario')
        clave = request.GET.get('clave')
        colegio = CustomUser.objects.get(nombre=usuario,clave=clave)
        serializer = CustomUserSerializer(colegio)
        print(len(serializer.data))
        return Response(serializer.data)
        

class EstudiantesList(APIView):
    def get(self,request):
        estudiantes = Estudiantes.objects.all()
        data = EstudiantesSerializer(estudiantes,many=True).data
        return Response(data)
    
class EstudiantesByColegio(APIView):
    def get(self, request, Idcolegio):
        estudiantes = Estudiantes.objects.filter(colegio=Idcolegio)
        data = EstudiantesSerializer(estudiantes,many=True).data
        return Response(data)
