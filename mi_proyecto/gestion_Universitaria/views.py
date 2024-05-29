from django.shortcuts import render, redirect
from .forms import AlumnoForm, CursoForm, NotasAlumnosPorCursoForm
from .models import Alumno, Curso, NotasAlumnosPorCurso

# Create your views here.
def agregar_alumno(request):
  if request.method == 'POST':
    form = AlumnoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('agregar_alumno')
  else:
    form = AlumnoForm()

  alumnos = Alumno.objects.all()
  return render(request, 'gestion_Universitaria/agregar_alumno.html', {'form': form, 'alumnos': alumnos})

def agregar_curso(request):
  if request.method == 'POST':
    form = CursoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('agregar_curso')
  else:
    form = CursoForm()
    
  cursos = Curso.objects.all()
  return render(request, 'gestion_Universitaria/agregar_curso.html', {'form': form, 'cursos': cursos})
  
def agregar_notas_alumnos_por_curso(request):
  if request.method == 'POST':
    form = NotasAlumnosPorCursoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('agregar_nota')
  else:
    form = NotasAlumnosPorCursoForm()
    
  notas = NotasAlumnosPorCurso.objects.all()
  return render(request, 'gestion_Universitaria/agregar_nota.html', {'form': form, 'notas': notas})