from django.contrib import admin
from .models import *

# Register your models here.


class UsuarioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'nacimiento')
    search_fields = ('nombre', 'nacimiento')


admin.site.register(Usuario, UsuarioAdmin)

class PosteoAdmin(admin.ModelAdmin):

    list_display = ('titulo', 'cuerpo')
    search_fields = ('titulo', 'cuerpo')


admin.site.register(Posteo, PosteoAdmin)

class ModeradorAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'sector')
    search_fields = ('nombre', 'sector')


admin.site.register(Moderador, ModeradorAdmin)
