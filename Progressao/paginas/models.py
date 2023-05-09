from django.db import models


class Cadastroaluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=True)
    datadenascimento = models.DateField(null=True, )
    ra = models.CharField(max_length=100, null=True)
    rg = models.CharField(max_length=100, null=True)

class Notas(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    ra = models.CharField(max_length=100, null=True)
    bimestre1_prova1 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    bimestre1_prova2 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    bimestre1_prova3 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    bimestre2_prova1 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    bimestre2_prova2 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    bimestre2_prova3 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    bimestre3_prova1 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    bimestre3_prova2 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    bimestre3_prova3 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    bimestre4_prova1 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    bimestre4_prova2 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    bimestre4_prova3 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    bimestre5_prova1 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    bimestre5_prova2 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    bimestre5_prova3 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    bimestre6_prova1 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    bimestre6_prova2 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    bimestre6_prova3 = models.DecimalField(max_digits=5, decimal_places=2, null=True)

