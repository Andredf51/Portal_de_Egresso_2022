from django.urls import path
from . import views
from .views import IndexView, listacursosview, listarturmasview, listaregressoview
from .views import EgressoAreaView, CoordenadorAreaView, GerenciarAlunos2View

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cursoselect/<str:curso_id>', views.listacursosview, name='curso_select'),
    path('turmaselect/<str:turma_id>', views.listarturmasview, name='turma_select'),
    path('egressoselect/<str:egresso_id>', views.listaregressoview, name='egresso_select'),

    path('egresso/', EgressoAreaView.as_view(), name='egresso'),
    path('coordenador/', CoordenadorAreaView.as_view(), name='coordenador'),
    path('gerenciaraluno/', views.GerenciarAlunos2View, name='gerenciaraluno'),

]