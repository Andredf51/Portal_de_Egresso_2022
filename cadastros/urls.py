#Página de cadastros

from django.urls import path
from .views import CursoCreate, TurmaCreate
from .views import CursoUpdate, TurmaUpdate
from .views import CursoDelete, TurmaDelete
from .views import CursoLista, TurmaLista

urlpatterns = [
    path('cadastrar/curso/', CursoCreate.as_view(), name='criar_curso'),
    path('cadastrar/turma/', TurmaCreate.as_view(), name='criar_turma'),

    path('editar/curso/<int:pk>/', CursoUpdate.as_view(), name='editar_curso'),
    path('editar/turma/<int:pk>/', TurmaUpdate.as_view(), name='editar_turma'),

    path('excluir/curso/<int:pk>/', CursoDelete.as_view(), name='excluir_curso'),
    path('excluir/turma/<int:pk>/', TurmaDelete.as_view(), name='excluir_turma'),

    path('listar/cursos/', CursoLista.as_view(), name='listar_cursos'),
    path('listar/turmas/', TurmaLista.as_view(), name='listar_turma'),

]