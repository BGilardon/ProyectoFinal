from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name= 'inicio' ),
    
    
    path('usuarios/', usuarios, name='usuarios'),
    path('usuariosCrear/', usuariosCrear, name='usuariosCrear' ),
    path('usuariosBuscar/', usuariosBuscar, name='usuariosBuscar' ),
    
    
    path('posteos/', posteos, name='posteos'),
    path('moderadores/', moderadores, name='moderadores'),
]
