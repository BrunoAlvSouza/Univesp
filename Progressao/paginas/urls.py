from django.urls import path
from .views import PaginaInicial, SobreView, CadastroalunoView, ListagemalunoView, aluno, alunos_json, excluir_aluno,NotasView, CadastronotaView, nota, ListagemnotaView

urlpatterns = [
    #path('endereço/', MinhaView.as_view(), name='nome_da_url')
    path('', PaginaInicial.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('cadastroaluno/', CadastroalunoView.as_view(), name='cadastroaluno'),
    path('listagemalunos/', ListagemalunoView.as_view(), name='listagemalunos'),
    path('listagemnotas/', ListagemnotaView.as_view(), name='listagemnotas'),
    path('alunos/', aluno, name='aluno'),
    path('nota/', nota, name='nota'),
    path('alunos_json/', alunos_json, name='alunos_json'),
    path('excluir_aluno/<int:id_aluno>/', excluir_aluno, name='excluir_aluno'),
    path('cadastronota/', CadastronotaView.as_view(), name='cadastronotas')
    ]