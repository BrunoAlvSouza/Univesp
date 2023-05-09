from django import forms
from .models import Cadastroaluno
from .models import Notas

class CadastroalunoForm(forms.ModelForm):
    class Meta:
        model = Cadastroaluno
        fields = ['nome', 'datadenascimento', 'ra', 'rg']
        
class NotasForm(forms.ModelForm):
    class Meta:
        model = Notas
        fields = ['nome', 'ra',
                  'bimestre1_prova1', 'bimestre1_prova2', 'bimestre1_prova3',
                  'bimestre2_prova1', 'bimestre2_prova2', 'bimestre2_prova3',
                  'bimestre3_prova1', 'bimestre3_prova2', 'bimestre3_prova3',
                  'bimestre4_prova1', 'bimestre4_prova2', 'bimestre4_prova3',
                  'bimestre5_prova1', 'bimestre5_prova2', 'bimestre5_prova3',
                  'bimestre6_prova1', 'bimestre6_prova2', 'bimestre6_prova3',
                  ]

