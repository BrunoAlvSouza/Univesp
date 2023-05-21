from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Cadastroaluno(models.Model):
    id_aluno = models.AutoField(primary_key=True, unique=True)
    cpf_aluno = models.CharField(max_length=11, null=False)
    nomecompleto_aluno = models.CharField(max_length=100, null=True)
    datadenascimento_aluno = models.DateField(null=True)
    rua_aluno = models.CharField(max_length=100, null=True)
    numero_aluno = models.CharField(max_length=100, null=True)
    bairro_aluno = models.CharField(max_length=100, null=True)
    municipio_aluno = models.CharField(max_length=100, null=True)
    nomemae_aluno = models.CharField(max_length=100, null=True)
    nomepai_aluno = models.CharField(max_length=100, null=True)
    classe_choices = [
        (1, 'turma1'),
        (2, 'turma2'),
        (3, 'turma3'),
        (4, 'turma4'),
        (5, 'turma5'),
        (6, 'turma6'),
    ]
    classe_aluno = models.CharField(max_length=100, choices=classe_choices, null=True)
    professor_aluno = models.CharField(max_length=100, null=True)
    
class Cadastroprofessor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    id_professor = models.AutoField(primary_key=True, unique=True)
    cpf_professor = models.CharField(max_length=11, null=False)
    nomecompleto_professor = models.CharField(max_length=100, null=True)
    datadenascimento_professor = models.DateField(null=True)
    rua_professor = models.CharField(max_length=100, null=True)
    numero_professor = models.CharField(max_length=100, null=True)
    bairro_professor = models.CharField(max_length=100, null=True)
    municipio_professor = models.CharField(max_length=100, null=True)
    formacao_professor = models.CharField(max_length=100, null=True)
    email_professor = models.EmailField(max_length=254, null=True)
    classe_choices_professor = [
        (1, 'turma1'),
        (2, 'turma2'),
        (3, 'turma3'),
        (4, 'turma4'),
        (5, 'turma5'),
        (6, 'turma6'),
    ]
    classe_professor = models.CharField(max_length=100, choices=classe_choices_professor, null=True)
    
class Notas(models.Model):
    id_nota = models.AutoField(primary_key=True)
    datahoje_nota = models.DateField(max_length=10, null=False)
    nomecompleto_nota = models.CharField(max_length=100, null=False)
    classe_nota = models.CharField(max_length=11, null=False)
    atividade_nota = models.CharField(max_length=255, null=True)
    nota_nota = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return f'{self.classe_nota} - {self.atividade_nota} - {self.nota}'

    
class Faltas(models.Model):
    id_falta = models.AutoField(primary_key=True, unique=True)
    datahoje_falta= models.DateField(null=True)
    nomecompleto_falta = models.CharField(max_length=100, null=False)
    classe_falta = models.CharField(max_length=11, null=False)
    escolhas_falta = [
        (1, 'F'),
        (2, 'P'),
    ]
    presenca_falta = models.CharField(max_length=10, choices=escolhas_falta, null=True)

    def __str__(self):
        return f'{self.cpf_faltas} - {self.data_faltas} - {self.presenca_faltas}'

