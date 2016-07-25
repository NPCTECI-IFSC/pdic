from .forms import UsuarioForm
from .models import Usuario
from django.contrib import admin


class UsuarioAdmin(admin.ModelAdmin):
    form = UsuarioForm

admin.site.register(Usuario, UsuarioAdmin)
