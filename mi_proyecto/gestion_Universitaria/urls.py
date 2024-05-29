from django.urls import path
from . import views

urlpatterns = [
  path('alumnos/', views.agregar_alumno, name='agregar_alumno'),
  path('cursos/', views.agregar_curso, name='agregar_curso'),
  path('notas/', views.agregar_notas_alumnos_por_curso, name='agregar_nota'),
]