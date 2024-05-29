import django import forms
import .models import Alumno, Curso, NotasAlumnosPorCurso

class AlumnoForm(forms.ModelForm):
  
  class Meta:
    model = Alumno
    fields = ['cui', 'nombre', 'apellidos', 'edad', 'dni']
    
class CursoForm(forms.ModelForm):

  class Meta:
    model = Curso
    fields = ['codigo', 'nombre']
    
class NotasAlumnosPorCursoForm(forms.ModelForm):
  alumno = forms.ModelChoiceField(queryset=Alumno.objects.all(), label='Alumno')
  
  class Meta:
    model = NotasAlumnosPorCurso
    fields = ['alumno', 'curso', 'notas']