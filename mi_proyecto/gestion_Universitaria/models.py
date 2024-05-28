from django.db import models

# Create your models here.
class Alumno(models.Model):
  cui = models.IntegerField(validators=[MinValueValidator(10000000), MaxValueValidator(99999999)], unique=True)
  nombre = models.CharField(max_length=100)
  apellidos = models.CharField(max_length=100)
  edad = models.IntegerField(max_value=100)
  dni = models.IntegerField(validators=[MinValueValidator(10000000), MaxValueValidator(99999999)])
  
  def __str__(self):
    return f"{self.nombre} {self.apellidos}"