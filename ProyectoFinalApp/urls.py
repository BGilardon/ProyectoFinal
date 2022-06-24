from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name= 'inicio' ),
    path('usuarios/', usuarios, name='usuarios'),
    path('crearUsuarios/', creaUsuarios, name='crearUsuario' ),
    path('posteos/', posteos, name='posteos'),
    path('moderadores/', moderadores, name='moderadores'),
]
