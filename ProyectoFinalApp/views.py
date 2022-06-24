from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def inicio(request):
    
    return render(request,'index.html')



def usuarios(request):
    
    return render(request,'usuarios.html')

def creaUsuarios(request):
        # post
    if request.method == "POST":
        
        formulario = crearUsuario(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            usuario = Usuario(nombre=info["nombre"],email=info["email"],nacimiento=info["nacimiento"]) # Error aca
            usuario.save()

            return redirect("crearUsuarios")

        return render(request,"crearUsuarios.html",{"form":formulario})

    # get
    formulario = crearUsuario()
    return render(request,"crearUsuarios.html",{"form":formulario})


def buscarUsuario(request):
    pass



def posteos(request):
    
    return render(request,'posteos.html')

def creaPosteos(request):
    pass

def buscarPosteos(request):
    pass



def moderadores(request):
    
    return render(request,'moderadores.html')

def creaModeradores(request):
    pass

def buscarModeradores(request):
    pass

