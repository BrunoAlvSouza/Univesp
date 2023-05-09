from django.urls import path
from django.contrib.auth import views as auth_views
from .views import PaginaInicial, CadastroprofessorView, registro, SobreView, ListagemturmaView, CadastroturmaView, CadastroalunoView, CadastrofaltaView,  AreadasecretariaView, ListagemfaltaView, ListagemalunoView, AreadoprofessorView, AreadoalunoView, NotasView, ListagemnotaView, CadastronotaView, cadastrar_professores, atualizar_lista_notas, salvar_notas, salvar_presenca, associar_aluno, atualizar_lista, turmas_json, cadastrar_notas, cadastrar_faltas, selecaoturma, cadastrar_alunos, excluir_aluno, excluir_falta, excluir_nota, faltas_json, aluno, alunos_json, notas_json, processar_lote

urlpatterns = [
    #path('endereço/', MinhaView.as_view(), name='nome_da_url')
    path('', auth_views.LoginView.as_view(template_name='paginas/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', registro, name='registro'),
    path('index', PaginaInicial.as_view(), name='index'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('areadoprofessor/', AreadoprofessorView.as_view(), name='areadoprofessor'),
    path('areadoaluno/', AreadoalunoView.as_view(), name='areadoaluno'),
    path('areadasecretaria/', AreadasecretariaView.as_view(), name='areadasecretaria'),
    path('cadastroaluno/', CadastroalunoView.as_view(), name='cadastroaluno'),
    path('cadastroprofessor/', CadastroprofessorView.as_view(), name='cadastroprofessor'),
    path('cadastrofalta/', CadastrofaltaView.as_view(), name='cadastrofalta'),
    path('cadastronota/', CadastronotaView.as_view(), name='cadastronota'),
    path('cadastroturma/', CadastroturmaView.as_view(), name='cadastroturma'),
    path('listagemalunos/', ListagemalunoView.as_view(), name='listagemalunos'),
    path('listagemnotas/', ListagemnotaView.as_view(), name='listagemnotas'),  
    path('listagemfaltas/', ListagemfaltaView.as_view(), name='listagemfaltas'),
    path('listagemturmas/', ListagemturmaView.as_view(), name='listagemturmas'),
    path('turmas_json/', turmas_json, name='turmas_json'),
    path('notas_json/', notas_json, name='notas_json'),
    path('faltas_json/', faltas_json, name='faltas_json'),
    path('alunos_json/', alunos_json, name='alunos_json'),
    path('cadastrar_notas/', cadastrar_notas, name='cadastrar_notas'),
    path('cadastrar_faltas/', cadastrar_faltas, name='cadastrar_faltas'),
    path('cadastrar_alunos/', cadastrar_alunos, name='cadastrar_alunos'),
    path('excluir_aluno/<int:id_aluno>/', excluir_aluno, name='excluir_aluno'),
    path('excluir_nota/<int:id_notas>/', excluir_nota, name='excluir_nota'),
    path('excluir_falta/<int:id_faltas>/', excluir_falta, name='excluir_falta'),
    path('associar_aluno/<int:id_aluno>/', associar_aluno, name='associar_aluno'),
    path('atualizar_lista/', atualizar_lista, name='atualizar_lista'),
    path('salvar_presenca/', salvar_presenca, name='salvar_presenca'),
    path('atualizar_lista_notas/', atualizar_lista_notas, name='atualizar_lista_notas'),
    path('salvar_notas/', salvar_notas, name='salvar_notas'),
    path('cadastrar_professores/', cadastrar_professores, name='cadastrar_professores')
    ]