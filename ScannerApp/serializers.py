from rest_framework import serializers
from .models import Estudiantes, Ingreso

class EstudiantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiantes
        fields = '__all__'  


class IngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingreso
        fields = '__all__'        