from django import forms

class Curso_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()

class Alumno_formulario(forms.Form):
    apellido = forms.CharField(max_length=30)
    nombre = forms.CharField(max_length=40)
    fecha_nac = forms.DateField()
    dni = forms.IntegerField()
    mail = forms.EmailField()

class Profesor_formulario(forms.Form):
    apellido = forms.CharField(max_length=30)
    nombre = forms.CharField(max_length=40)
    mail = forms.EmailField()
    profesion = forms.CharField(max_length=100)

class Entregable_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    fecha_entrega = forms.DateField()
    entregado = forms.BooleanField()