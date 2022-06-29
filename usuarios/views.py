#Página para a criação de usuários

from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from .forms import AlunoForm, CoordenadorForm
from django.urls import reverse_lazy

#método utilizado para filtrar os usuários
from django.shortcuts import get_object_or_404

#método para editar os usuários
from .models import PerfilAluno, PerfilCoordenador

class AlunoCreate(CreateView):
    template_name = 'cadastros/form.html'
    form_class = AlunoForm
    success_url = reverse_lazy('login')

    #função para adicionar o usuário em um grupo
    def form_valid(self, form):

        grupo = get_object_or_404(Group, name='Egresso')

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        PerfilAluno.objects.create(usuario_aluno=self.object)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Registro de novo usuário'
        context['botao'] = 'Cadastrar'

        return context


class PerfilAlunoUpdate(UpdateView):
    template_name = 'cadastros/form.html'
    model = PerfilAluno
    fields = ['nome_completo', 'curso', 'turma', 'cargo_atual', 'foto', 'empresa_atual', 'trabalha_area', 'ifb_ajudou',
              'grade_ifb', 'curso_extra', 'qual_curso_extra', 'opiniao_curso_ifb', 'pode_melhorar', 'rede_social', 'lattes']
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(PerfilAluno, usuario_aluno=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Meus dados pessoais de egresso'
        context['botao'] = "Atualizar"

        return context


class CoordenadorCreate(CreateView):
    template_name = 'cadastros/form.html'
    form_class = CoordenadorForm
    success_url = reverse_lazy('login')

    #função para adicionar o usuário em um grupo
    def form_valid(self, form):

        grupo = get_object_or_404(Group, name='Coordenador')

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        PerfilCoordenador.objects.create(usuario_coordenador=self.object)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Registro de novo coordenador'
        context['botao'] = 'Cadastrar'

        return context


class PerfilCoordenadorUpdate(UpdateView):
    template_name = 'cadastros/form.html'
    model = PerfilCoordenador
    fields = ['nome_completo', 'curso', 'telefone']
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(PerfilCoordenador, usuario_coordenador=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Meus dados pessoais de coordenador'
        context['botao'] = "Atualizar"

        return context