#Banco de dados de usuários

from django.db import models
from django.contrib.auth.models import User

from cadastros.models import Curso, Turma

class PerfilAluno(models.Model):
    TrabalhaArea_CHOICES = (
        ('Sim', 'Sim'),
        ('Nao', 'Não'),
        ('EmParte', 'Em parte'),
    )
    CursoExtra_CHOICES = (
        ('Sim', 'Sim'),
        ('Nao', 'Não'),
    )
    Validador_CHOICES = (
        ('Sim', 'Sim'),
        ('Nao', 'Não'),
    )

    nome_completo = models.CharField(max_length=150, null=True)
    curso = models.CharField(max_length=50, null=True)
    cargo_atual = models.CharField(max_length=50, null=True)

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, null=True)

    foto = models.CharField(max_length=150, null=True)
    empresa_atual = models.CharField(max_length=50, null=True)
    trabalha_area = models.CharField(max_length=8, choices=TrabalhaArea_CHOICES, null=True)
    ifb_ajudou = models.CharField(max_length=8, choices=TrabalhaArea_CHOICES, null=True)
    grade_ifb = models.CharField(max_length=10, null=True)
    curso_extra = models.CharField(max_length=10, choices=CursoExtra_CHOICES, null=True)
    qual_curso_extra = models.CharField(max_length=30, null=True)
    opiniao_curso_ifb = models.CharField(max_length=100, null=True)
    pode_melhorar = models.CharField(max_length=100, null=True)
    rede_social = models.CharField(max_length=100, null=True)
    lattes = models.CharField(max_length=100, null=True)
    validado = models.CharField(max_length=5, choices=Validador_CHOICES, null=True)

    usuario_aluno = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_completo


class PerfilCoordenador(models.Model):
    nome_completo = models.CharField(max_length=70, null=True)
    email = models.EmailField(max_length=70, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)
    telefone = models.CharField(max_length=12, null=True)

    usuario_coordenador = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_completo

#Esquema do banco de dados
# 1 - 1 - OneToOneField
# 1 - n - ForeignKey (One to Many)
# n - n - ManyToManyField