from django.urls import path
from .views import EstudiantesList, EstudiantesDetail, IngresoList, IngresoDetail

urlpatterns = [
    path('v1/estudiantes/', EstudiantesList.as_view(), name='estudiantes-list'),
    path('v1/estudiantes/<int:pk>/', EstudiantesDetail.as_view(), name='estudiantes-detail'),
    path('v1/ingreso/', IngresoList.as_view(), name='ingreso-list'),
    path('v1/ingreso/<int:pk>/', IngresoDetail.as_view(), name='ingreso-detail'),
]