from django.contrib import admin
from .models import Estudiantes, Ingreso

@admin.register(Estudiantes)
class EstudiantesAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'codigo', 'correo', 'semestre')
    search_fields = ('nombres', 'codigo', 'correo')
    list_filter = ('semestre',)

@admin.register(Ingreso)
class IngresoAdmin(admin.ModelAdmin):
    list_display = ('idestudiante', 'fecha_ingreso', 'hora_ingreso')
    list_filter = ('fecha_ingreso',)
    search_fields = ('idestudiante__nombres',)
