from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre} Camada: {self.camada}"

class Alumno(models.Model):
    apellido = models.CharField(max_length=30)
    nombre = models.CharField(max_length=40)
    fecha_nac = models.DateField()
    dni = models.IntegerField()
    mail = models.EmailField()
    def __str__(self):
        return f"Apellido: {self.apellido} Nombre: {self.nombre} Fecha_Nac.: {self.fecha_nac} Dni: {self.dni} Mail: {self.mail}"

class Profesor(models.Model):
    apellido = models.CharField(max_length=30)
    nombre = models.CharField(max_length=40)
    mail = models.EmailField()
    profesion = models.CharField(max_length=100)
    def __str__(self):
        return f"Apellido: {self.apellido} Nombre: {self.nombre} Mail: {self.mail} Profesion: {self.profesion}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()
    def __str__(self):
        return f"Nombre: {self.nombre} Fecha Entrega: {self.fecha_entrega} Entregado: {self.entregado}"
