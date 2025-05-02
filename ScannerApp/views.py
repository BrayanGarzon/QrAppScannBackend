from django.shortcuts import render
from rest_framework import generics
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from .models import Estudiantes, Ingreso
from .serializers import EstudiantesSerializer, IngresoSerializer

def home(request):
    return render(request, 'home.html')

@extend_schema(
    summary="Lista los estudiantes registrados",
    description="Este endpoint devuelve todos los estudiantes actualmente registrados en el sistema.",
    parameters=[
        OpenApiParameter("buscar", str, OpenApiParameter.QUERY, description="Filtro de búsqueda por nombre o código")
    ],
    responses={200: EstudiantesSerializer(many=True)},
    examples=[
        OpenApiExample(
            "Respuesta de ejemplo",
            value=[{"id": 1, "nombre": "Juan Pérez", "codigo": "12345"}]
        )
    ]
)
class EstudiantesList(generics.ListCreateAPIView):
    queryset = Estudiantes.objects.all()
    serializer_class = EstudiantesSerializer

@extend_schema(
    summary="Obtiene el detalle de un estudiante",
    description="Este endpoint devuelve la información detallada de un estudiante específico, dado su ID.",
    responses={200: EstudiantesSerializer},
    examples=[
        OpenApiExample(
            "Respuesta de ejemplo",
            value={"id": 1, "nombre": "Juan Pérez", "codigo": "12345"}
        )
    ]
)
class EstudiantesDetail(generics.RetrieveAPIView):
    queryset = Estudiantes.objects.all()
    serializer_class = EstudiantesSerializer    

@extend_schema(
    summary="Lista los ingresos registrados",
    description="Este endpoint devuelve todos los ingresos registrados en el sistema.",
    responses={200: IngresoSerializer(many=True)},
    examples=[
        OpenApiExample(
            "Respuesta de ejemplo",
            value=[{"id": 1, "estudiante": 1, "fecha": "2025-05-02T12:00:00Z"}]
        )
    ]
)
class IngresoList(generics.ListCreateAPIView):
    queryset = Ingreso.objects.all()
    serializer_class = IngresoSerializer 

@extend_schema(
    summary="Obtiene el detalle de un ingreso",
    description="Este endpoint devuelve la información detallada de un ingreso específico, dado su ID.",
    responses={200: IngresoSerializer},
    examples=[
        OpenApiExample(
            "Respuesta de ejemplo",
            value={"id": 1, "estudiante": 1, "fecha": "2025-05-02T12:00:00Z"}
        )
    ]
)
class IngresoDetail(generics.RetrieveAPIView):
    queryset = Ingreso.objects.all()
    serializer_class = IngresoSerializer
