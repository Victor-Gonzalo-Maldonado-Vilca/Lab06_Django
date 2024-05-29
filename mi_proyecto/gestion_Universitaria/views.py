from django.shortcuts import render, redirect
from .forms import AlumnoForm, CursoForm, NotasAlumnosPorCursoForm

# Create your views here.
def agregar_alumno(request):
  if request.method == 'POST':
    form = AlumnoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('table_alumnos')
  else:
    form = AlumnoForm()
  return render(request, 'gestion_Universitaria/agregar_alumno.html', {'form': form})
    