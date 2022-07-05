#Painel administrativo

from django.contrib import admin

# Importar as classes
from .models import Curso, Turma

# Modelos

class DetalhesTurmaAdmin(admin.ModelAdmin):
    list_display = ('periodo', 'curso')


admin.site.register(Curso)
admin.site.register(Turma, DetalhesTurmaAdmin)
