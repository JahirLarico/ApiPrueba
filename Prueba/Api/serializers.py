from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class EstudiantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiantes
        fields = ['id','nombreEstudiante','apellidoEstudiante','edad','nombreApoderado','celularApoderado','correoApoderado']

class CustomUserSerializer(serializers.ModelSerializer):
    estudiantes = EstudiantesSerializer(many=True,read_only=True)
    class Meta:
        model = CustomUser
        fields = ['id','username','clave','nombre','estudiantes']