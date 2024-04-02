from django.shortcuts import render
from AppCoder.models import Curso, Alumno, Profesor, Entregable
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario, Alumno_formulario, Profesor_formulario, Entregable_formulario

# Create your views here.

def inicio(request):
    return render(request, "buscar_camada.html")

def buscarc(request):
    if request.GET["camada"]:
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains= camada)
        return render( request , "rb_camada.html" , {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre de la camada")


# -------------------------------------------------------------------------------------------------
# VIEWS DE CURSO
# -------------------------------------------------------------------------------------------------

def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def curso_formulario(request):
    if request.method == "POST":
        mi_formulario = Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso(nombre=datos["nombre"], camada=datos["camada"])
            curso.save()
            return render(request, "frm_curso.html")
    return render(request, "frm_curso.html")

def confirma_eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    return render(request, "eliminar_curso.html", {"cursos":curso})

def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    curso = Curso.objects.all()
    return render(request, "cursos.html", {"cursos":curso})

def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save()
            cursos = Curso.objects.all()
            return render(request, "cursos.html", {"cursos":cursos})
    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre, "camada":curso.camada})
    return render(request, "editar_curso.html", {"mi_formulario":mi_formulario, "curso":curso})

def buscar_curso(request):
    return render(request, "buscar_curso.html")

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        return render( request , "rb_curso.html" , {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")

# -------------------------------------------------------------------------------------------------
# VIEWS DE ALUMNO
# -------------------------------------------------------------------------------------------------

def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    dicc = {"alumnos": alumnos}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def alumno_formulario(request):
    if request.method == "POST":
        mi_formulario = Alumno_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno = Alumno(apellido=datos["apellido"], nombre=datos["nombre"], fecha_nac=datos["fecha_nac"], dni=datos["dni"], mail=datos["mail"])
            alumno.save()
            return render(request, "frm_alumno.html")
    return render(request, "frm_alumno.html")

def eliminar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    alumno = Alumno.objects.all()
    return render(request, "alumnos.html", {"alumnos":alumno})

def editar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Alumno_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno.apellido = datos["apellido"]
            alumno.nombre = datos["nombre"]
            alumno.fecha_nac = datos["fecha_nac"]
            alumno.dni = datos["dni"]
            alumno.mail = datos["mail"]
            alumno.save()
            alumnos = Alumno.objects.all()
            return render(request, "alumnos.html", {"alumnos":alumnos})
    else:
        mi_formulario = Alumno_formulario(initial={"nombre":alumno.nombre, "fecha_nac":alumno.fecha_nac, "dni":alumno.dni, "mail":alumno.mail})
    return render(request, "editar_alumno.html", {"mi_formulario":mi_formulario, "alumno":alumno})

def buscar_alumno(request):
    return render(request, "buscar_alumno.html")

def buscara(request):
    if request.GET["apellido"]:
        apellido = request.GET["apellido"]
        alumnos = Alumno.objects.filter(apellido__icontains= apellido)
        return render( request , "rb_alumno.html" , {"alumnos":alumnos})
    else:
        return HttpResponse("Ingrese el nombre del alumno")

# -------------------------------------------------------------------------------------------------
# VIEWS DE PROFESOR
# -------------------------------------------------------------------------------------------------

def ver_profesores(request):
    profesores = Profesor.objects.all()
    dicc = {"profesores": profesores}
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def profesor_formulario(request):
    if request.method == "POST":
        mi_formulario = Profesor_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor = Profesor(apellido=datos["apellido"], nombre=datos["nombre"], mail=datos["mail"], profesion=datos["profesion"])
            profesor.save()
            return render(request, "frm_profesor.html")
    return render(request, "frm_profesor.html")

def eliminar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    profesor = Profesor.objects.all()
    return render(request, "profesores.html", {"profesores":profesor})

def editar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Profesor_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor.apellido = datos["apellido"]
            profesor.nombre = datos["nombre"]
            profesor.mail = datos["mail"]
            profesor.profesion = datos["profesion"]
            profesor.save()
            profesores = Profesor.objects.all()
            return render(request, "profesores.html", {"profesores":profesores})
    else:
        mi_formulario = Profesor_formulario(initial={"apellido":profesor.apellido, "nombre":profesor.nombre, "mail":profesor.mail, "profesion":profesor.profesion})
    return render(request, "editar_profesor.html", {"mi_formulario":mi_formulario, "profesor":profesor})

def buscar_profesor(request):
    return render(request, "buscar_profesor.html")

def buscarp(request):
    if request.GET["apellido"]:
        apellido = request.GET["apellido"]
        profesores = Profesor.objects.filter(apellido__icontains= apellido)
        return render( request , "rb_profesor.html" , {"profesores":profesores})
    else:
        return HttpResponse("Ingrese el nombre del profesor")

# -------------------------------------------------------------------------------------------------
# VIEWS DE ENTREGABLE
# -------------------------------------------------------------------------------------------------

def ver_entregables(request):
    entregables = Entregable.objects.all()
    dicc = {"entregables": entregables}
    plantilla = loader.get_template("entregables.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def entregable_formulario(request):
    if request.method == "POST":
        mi_formulario = Entregable_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            entregable = Entregable(nombre=datos["nombre"], fecha_entrega=datos["fecha_entrega"], entregado=datos["entregado"])
            entregable.save()
            return render(request, "frm_entregable.html")
    return render(request, "frm_entregable.html")

def eliminar_entregable(request, id):
    entregable = Entregable.objects.get(id=id)
    entregable.delete()
    entregable = Entregable.objects.all()
    return render(request, "entregables.html", {"entregables":entregable})

def editar_entregable(request, id):
    entregable = Entregable.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Entregable_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            entregable.nombre = datos["nombre"]
            entregable.fecha_entrega = datos["fecha_entrega"]
            entregable.entregado = datos["entregado"]
            entregable.save()
            entregables = Entregable.objects.all()
            return render(request, "entregables.html", {"entregables":entregables})
    else:
        mi_formulario = Entregable_formulario(initial={"nombre":entregable.nombre, "fecha_entrega":entregable.fecha_entrega, "entregado":entregable.entregado})
    return render(request, "editar_entregable.html", {"mi_formulario":mi_formulario, "entregable":entregable})

def buscar_entregable(request):
    return render(request, "buscar_entregable.html")

def buscare(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        entregables = Entregable.objects.filter(nombre__icontains= nombre)
        return render( request , "rb_entregable.html" , {"entregables":entregables})
    else:
        return HttpResponse("Ingrese el nombre del entregable")
