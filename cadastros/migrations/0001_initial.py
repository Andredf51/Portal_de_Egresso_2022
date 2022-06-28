# Generated by Django 4.0.4 on 2022-06-27 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('nivel', models.CharField(choices=[('Superior', 'Superior (Bacharelado / Licenciatura)'), ('Superior', 'Superior (Tecnologia)'), ('Tecnico', 'Técnico (Integrado)'), ('Tecnico', 'Técnico(Subsequente)')], max_length=255, verbose_name='nível')),
                ('campus', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(max_length=255, verbose_name='Período')),
                ('data_formatura', models.CharField(max_length=255)),
                ('foto', models.CharField(max_length=255)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.curso')),
            ],
        ),
    ]
