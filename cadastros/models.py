#Modelo de Banco de dados Cadastros

from django.db import models

#Primeiros das tabela sem relacionamentos

class Curso(models.Model):
    NIVEL_CHOICES = (
        ('Superior', 'Superior (Bacharelado / Licenciatura)'),
        ('Superior', 'Superior (Tecnologia)'),
        ('Tecnico', 'Técnico (Integrado)'),
        ('Tecnico', 'Técnico(Subsequente)'),
    )

    nome = models.CharField(max_length=255, null=False)
    nivel = models.CharField(max_length=255, verbose_name='nível', choices=NIVEL_CHOICES, null=False)
    campus = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.nome


#Agora usar as tabelas com relacionamentos

class Turma(models.Model):

    periodo = models.CharField(max_length=255, verbose_name='Período', null=False)
    data_formatura = models.CharField(max_length=255, null=False)
    foto = models.CharField(max_length=255, null=False)

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.periodo

#Esquema do banco de dados
# 1 - 1 - OneToOneField
# 1 - n - ForeignKey (One to Many)
# n - n - ManyToManyField