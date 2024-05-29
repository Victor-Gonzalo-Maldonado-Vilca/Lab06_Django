from django.shortcuts import render, redirect
from .forms import AlumnoForm, CursoForm, NotasAlumnosPorCursoForm

# Create your views here.
def agregar_alumno(request):
  if request.method == 'POST':
    form = AlumnoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('lista_alumnos')
  else:
    form = AlumnoForm()
  return render(request, 'gestion_Universitaria/agregar_alumno.html', {'form': form})
    
def agregar_curso(request):
  if request.method == 'POST'
    form = CursoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('lista_cursos')
  else:
    form = CursoForm()
  return render(request, 'gestion_Universitaria/agregar_curso.html', {'form': form})
  
def agregar_NotasAlumnosPorCursoForm(request):
  if request.method == 'POST'
    form = NotasAlumnosPorCursoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('notas_alumnos')
  else:
    form = NotasAlumnosPorCursoForm()
  return render(request, 'gestion_Universitaria/agregar_notas.html', {'form': form})