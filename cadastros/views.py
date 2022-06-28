#códico para CRUD do sistema

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Curso, Turma

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin


################# Cursos ###############################
class CursoLista(ListView):
    models = Curso
    template_name = 'cadastros/listas/cursos.html'
    queryset = Curso.objects.all()
    context_object_name = 'listarcursos'


class CursoCreate(CreateView):

    model = Curso
    template_name = 'cadastros/form.html'
    fields = ['nome', 'nivel', 'campus']
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Cadastro de Cursos'
        context['botao'] = 'Cadastrar'

        return context


class CursoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Curso
    template_name = 'cadastros/form.html'
    fields = ['nome', 'nivel', 'campus']
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Atualização de Cursos'
        context['botao'] = 'Salvar'

        return context


class CursoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Curso
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')


################# Turmas ###############################

class TurmaLista(ListView):
    models = Turma
    template_name = 'cadastros/listas/turmas.html'
    queryset = Turma.objects.all()
    context_object_name = 'listarturmas'


class TurmaCreate(CreateView):

    model = Turma
    fields = ['periodo', 'data_formatura', 'foto', 'curso']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Cadastro de Turmas'
        context['botao'] = 'Cadastrar'

        return context


class TurmaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Turma
    fields = ['periodo', 'data_formatura', 'foto', 'curso']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Atualização de Turmas'
        context['botao'] = 'Salvar'

        return context


class TurmaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Turma
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')