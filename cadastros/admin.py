#Painel administrativo

from django.contrib import admin

# Importar as classes
from .models import Curso, Turma

# Modelos
admin.site.register(Curso)
admin.site.register(Turma)
