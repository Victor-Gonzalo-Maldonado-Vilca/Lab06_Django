from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Alumno(models.Model):
  cui = models.IntegerField(validators=[MinValueValidator(10000000), MaxValueValidator(99999999)], unique=True)
  nombre = models.CharField(max_length=100)
  apellidos = models.CharField(max_length=100)
  edad = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
  dni = models.IntegerField(validators=[MinValueValidator(10000000), MaxValueValidator(99999999)])
  
  def __str__(self):
    return f"{self.nombre} {self.apellidos}"

class Curso(models.Model):
  codigo = models.IntegerField(validators=[MinValueValidator(1000000), MaxValueValidator(9999999)])
  nombre = models.CharField(max_length=100)
  
  def __str__(self):
    return self.nombre
   
class NotasAlumnosPorCurso(models.Model):
  alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
  curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
  notas = models.DecimalField(max_digits=5, decimal_places=2)
  
  def __str__(self):
    return f"La nota del Alumno: {self.alumno.nombre} {self.alumno.apellidos}, es = {self.notas}"
