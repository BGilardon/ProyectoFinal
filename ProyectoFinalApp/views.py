from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models import Q

# Create your views here.

# Inicio
def inicio(request):
    
    return render(request,'index.html')

def redirec(request):
    return render(request, 'redirec.html')


# Usuarios
def usuarios(request):
    
    usuarios = Usuario.objects.all()
    
    return render(request,'usuarios.html', {'usuarios':usuarios})



def usuariosCrear(request):
        # post
    if request.method == "POST":
        
        formulario = usuarioCrear(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            usuario = Usuario(nombre=info["nombre"],mail=info["mail"],nacimiento=info["nacimiento"])
            usuario.save()

            return redirect("usuariosCrear")

        return render(request,"usuariosCrear.html",{"form":formulario})

    # get
    formulario = usuarioCrear()
    return render(request,"usuariosCrear.html",{"form":formulario})


def usuariosBuscar(request):
    
    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            usuarios = Usuario.objects.filter( Q(nombre__icontains=search) | Q(nacimiento__icontains=search) ).values()

            return render(request,"usuariosBuscar.html",{"usuarios":usuarios, "search":True, "busqueda":search})

        else:
        
            usuarios = Usuario.objects.all()

            return render(request,"usuariosBuscar.html",{"usuarios":usuarios, "search":False})
    
    else:
        
        usuarios = Usuario.objects.all()

        return render(request,"usuariosBuscar.html",{"usuarios":usuarios, "search":False})



# Posteos

def posteos(request):
    
    return render(request,'posteos.html')

def creaPosteos(request):
    pass

def buscarPosteos(request):
    pass


# Moderadores

def moderadores(request):
    
    return render(request,'moderadores.html')

def creaModeradores(request):
    pass

def buscarModeradores(request):
    pass

