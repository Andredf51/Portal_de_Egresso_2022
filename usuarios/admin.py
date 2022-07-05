from django.contrib import admin
from .models import PerfilAluno, PerfilCoordenador


class TitulosAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'validado')

admin.site.register(PerfilAluno, TitulosAdmin)
admin.site.register(PerfilCoordenador)
