from django.urls import path
from django.contrib.auth import views as auth_views
from .views import AlunoCreate, CoordenadorCreate, PerfilAlunoUpdate, PerfilCoordenadorUpdate

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/form_login_personalizado.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registraraluno/', AlunoCreate.as_view(), name='registraraluno'),
    path('registrarcoordenador/', CoordenadorCreate.as_view(), name='registrarcoordenador'),
    path('atualizar_dados_aluno/', PerfilAlunoUpdate.as_view(), name='atualizar_dados_aluno'),
    path('atualizar_dados_coordenador/', PerfilCoordenadorUpdate.as_view(), name='atualizar_dados_coordenador'),
]