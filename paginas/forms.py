from django import forms
from .models import Cadastroaluno
from .models import Notas
from .models import Faltas

class CadastroalunoForm(forms.ModelForm):
    class Meta:
        model = Cadastroaluno
        fields = ['cpf_notas', 'nomecompleto_aluno', 'datadenascimento_aluno', 'rua_aluno', 'numero_aluno', 'bairro_aluno', 'municipio_aluno', 'nomemae_aluno', 'nomepai_aluno']
        
class NotasForm(forms.ModelForm):
    class Meta:
        model = Notas
        fields = ['cpf_notas', 'bimestre','atividade', 'nota'
                  ]

class FaltasForm(forms.ModelForm):
    class Meta:
        model = Faltas
        fields = '__all__'

