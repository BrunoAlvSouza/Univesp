from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Cadastroaluno
from .models import Cadastroprofessor
from .models import Notas
from .models import Faltas
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.core import serializers
from datetime import date
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import date
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login




class PaginaInicial(TemplateView):
    template_name= "paginas/index.html"
    
class SobreView(TemplateView):
    template_name="paginas/sobre.html"

class CadastroalunoView(TemplateView):
    template_name="paginas/cadastroaluno.html"
    
class CadastroprofessorView(TemplateView):
    template_name="paginas/cadastroprofessor.html"
    
class CadastronotaView(TemplateView):
    template_name="paginas/cadastronota.html"
    
class CadastrofaltaView(TemplateView):
    template_name="paginas/cadastrofalta.html"
    
class NotasView(TemplateView):
    template_name="paginas/notas.html"
    
class AreadoprofessorView(TemplateView):
    template_name="paginas/areadoprofessor.html"
    
class AreadasecretariaView(TemplateView):
    template_name="paginas/areadasecretaria.html"
    
class AreadoalunoView(TemplateView):
    template_name="paginas/areadoaluno.html"

class CadastroturmaView(TemplateView):
    template_name="paginas/cadastroturma.html"

def selecaoturma(request):
    alunos = Cadastroaluno.objects.all()
    context = {'alunos': alunos}
    return render(request, 'selecaoturma.html', context)

  
def aluno(request):
    if request.method=='POST':
        novo_aluno = Cadastroaluno()
        novo_aluno.nome = request.POST.get('nome')
        novo_aluno.ra = request.POST.get('ra')
        novo_aluno.rg = request.POST.get('rg')
        novo_aluno.datadenascimento = request.POST.get('datadenascimento')
        novo_aluno.save()
    return redirect('/listagemalunos/')

def alunos_json(request):
    alunos = Cadastroaluno.objects.all()
    data = []
    for aluno in alunos:
        data.append({
            'id_aluno': aluno.id_aluno,
            'nome': aluno.nome,
            'ra': aluno.ra,
            'datadenascimento': aluno.datadenascimento,
            'rg': aluno.rg
        })
    return JsonResponse({'data': data})

class ListagemalunoView(TemplateView):
    template_name = "paginas/listagemalunos.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        alunos = Cadastroaluno.objects.all()
        context["alunos"] = alunos
        return context

def processar_lote(request):
    if request.method == 'POST':
        classe = request.POST.get('classe')
        periodo = request.POST.get('alunos')
        # adicione outros campos aqui
        for i in range(25):
            aluno = Cadastroaluno(classe=classe, aluno=aluno)
            # adicione outros campos aqui
            aluno.save()
        return render(request, 'sucesso.html')
    else:
        return render(request, 'formulario_lote.html')

    
class ListagemnotaView(TemplateView):
    template_name = "paginas/listagemnotas.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        notas = Notas.objects.all()
        context["notas"] = notas
        return context
    
class ListagemfaltaView(TemplateView):
    template_name = "paginas/listagemfaltas.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        faltas = Faltas.objects.all()
        context["faltas"] = faltas
        return context

class ListagemturmaView(TemplateView):
    template_name = "paginas/listagemturmas.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        turmas = Cadastroaluno.objects.all()
        context["turma"] = turmas
        return context

def cadastrar_notas(request):
    if request.method == 'POST':
        cpf_notas = request.POST['cpf_notas']
        bimestre = request.POST['bimestre']
        atividade = request.POST['atividade']
        nota = request.POST['nota']
        notas = Notas(cpf_notas=cpf_notas, bimestre=bimestre, atividade=atividade, nota=nota)
        print(cpf_notas, bimestre, atividade, nota)
        notas.save()
        return redirect('/cadastronota/')
    
def cadastrar_faltas(request):
    if request.method == 'POST':
        cpf_faltas = request.POST['cpf_faltas']
        data_faltas = request.POST['data_faltas']
        presenca_faltas = request.POST['presenca_faltas']
        faltas = Faltas(cpf_faltas=cpf_faltas, data_faltas=data_faltas, presenca_faltas=presenca_faltas)
        print(cpf_faltas, data_faltas, presenca_faltas)
        faltas.save()
        return redirect('/cadastrofalta/')
    
def cadastrar_alunos(request):
    if request.method == 'POST':
        cpf_aluno = request.POST['cpf_aluno']
        nomecompleto_aluno = request.POST['nomecompleto_aluno']
        datadenascimento_aluno = request.POST['datadenascimento_aluno']
        rua_aluno = request.POST['rua_aluno']
        numero_aluno = request.POST['numero_aluno']
        bairro_aluno = request.POST['bairro_aluno']
        municipio_aluno = request.POST['municipio_aluno']
        nomemae_aluno = request.POST['nomemae_aluno']
        nomepai_aluno = request.POST['nomepai_aluno']
        print( cpf_aluno, nomecompleto_aluno, datadenascimento_aluno, rua_aluno, numero_aluno, bairro_aluno, municipio_aluno, nomemae_aluno, nomepai_aluno)
        cadastro = Cadastroaluno(cpf_aluno=cpf_aluno, nomecompleto_aluno=nomecompleto_aluno, datadenascimento_aluno=datadenascimento_aluno, rua_aluno=rua_aluno, numero_aluno=numero_aluno, bairro_aluno=bairro_aluno, municipio_aluno=municipio_aluno, nomemae_aluno=nomemae_aluno, nomepai_aluno=nomepai_aluno)
        cadastro.save()
        return redirect('/cadastroaluno/')

def cadastrar_professores(request):
    if request.method == 'POST':
        cpf_professor = request.POST['cpf_professor']
        nomecompleto_professor = request.POST['nomecompleto_professor']
        datadenascimento_professor = request.POST['datadenascimento_professor']
        rua_professor = request.POST['rua_professor']
        numero_professor = request.POST['numero_professor']
        bairro_professor = request.POST['bairro_professor']
        municipio_professor = request.POST['municipio_professor']
        formacao_professor = request.POST['formacao_professor']
        email_professor = request.POST['email_professor']

        cadastro = Cadastroprofessor(
            cpf_professor=cpf_professor,
            nomecompleto_professor=nomecompleto_professor,
            datadenascimento_professor=datadenascimento_professor,
            rua_professor=rua_professor,
            numero_professor=numero_professor,
            bairro_professor=bairro_professor,
            municipio_professor=municipio_professor,
            formacao_professor=formacao_professor,
            email_professor=email_professor
        )
        cadastro.save()
        return redirect('/cadastroprofessor/')


def notas_json(request):
    hoje = date.today()
    notas = Notas.objects.filter(datahoje_nota=hoje)
    data = {'data': []}
    for nota in notas:
        datahoje_formatado = nota.datahoje_nota.strftime('%d-%m-%Y')
        data['data'].append({
            'id_nota': nota.id_nota,
            'datahoje_nota': datahoje_formatado,
            'nomecompleto_nota': nota.nomecompleto_nota,
            'classe_nota': nota.classe_nota,
            'atividade_nota': nota.atividade_nota,
            'nota_nota': str(nota.nota_nota)
        })
    return JsonResponse(data)


def faltas_json(request):
    hoje = date.today()
    faltas = Faltas.objects.filter(datahoje_falta=hoje)
    data = {'data': []}
    for falta in faltas:
        datahoje_formatado = falta.datahoje_falta.strftime('%d-%m-%Y')
        data['data'].append({
            'id_falta': falta.id_falta,
            'datahoje_falta': datahoje_formatado,
            'nomecompleto_falta': falta.nomecompleto_falta,
            'classe_falta': falta.classe_falta,
            'presenca_falta':falta.presenca_falta
            
        })
    return JsonResponse(data)




def alunos_json(request):
    alunos = Cadastroaluno.objects.all()
    data = {
        'data': [
            {
                'id_aluno': aluno.id_aluno,
                'cpf_aluno': aluno.cpf_aluno,
                'nomecompleto_aluno': aluno.nomecompleto_aluno,
                'datadenascimento_aluno': aluno.datadenascimento_aluno.strftime('%d/%m/%Y'),
                'rua_aluno': aluno.rua_aluno,
                'numero_aluno': aluno.numero_aluno,
                'bairro_aluno': aluno.bairro_aluno,
                'municipio_aluno': aluno.municipio_aluno,
                'nomemae_aluno': aluno.nomemae_aluno,
                'nomepai_aluno': aluno.nomepai_aluno,
            } for aluno in alunos
        ]
    }
    return JsonResponse(data)

def excluir_aluno(request, id_aluno):
    aluno = get_object_or_404(Cadastroaluno, id_aluno=id_aluno)
    aluno.delete()
    return redirect('listagemalunos')

def excluir_nota(request, id_notas):
    nota = get_object_or_404(Notas, id_notas=id_notas)
    nota.delete()
    return redirect('listagemnotas')

def excluir_falta(request, id_faltas):
    falta = get_object_or_404(Faltas, id_faltas=id_faltas)
    falta.delete()
    return redirect('listagemfaltas')

#Busca os dados do Cadastro aluno para aparecer na página de cadastro de turmas 
def turmas_json(request):
    turmas = Cadastroaluno.objects.all()
    data = {'data': []}
    for turma in turmas:
        data['data'].append({
            'id_turma': turma.id_aluno,
            'cpf_turma': turma.cpf_aluno,
            'nomecompleto_turma': turma.nomecompleto_aluno,
            'classe_turma_atual': turma.classe_aluno,
            'bairro_aluno':turma.bairro_aluno
        })  
    return JsonResponse(data)

#Salva o dado no banco em Classe
def associar_aluno(request, id_aluno):
    classe = request.POST['classe_turma']
    print(classe)
    aluno = Cadastroaluno.objects.get(pk=id_aluno)
    aluno.classe_aluno = classe
    aluno.save()
    return redirect('listagemturmas')

def atualizar_lista(request):
    dados_aluno = Cadastroaluno.objects.all()

    for dado_aluno in dados_aluno:
        dados_falta, created = Faltas.objects.get_or_create(
            nomecompleto_falta=dado_aluno.nomecompleto_aluno,
            classe_falta=dado_aluno.classe_aluno,
            datahoje_falta=date.today()
        )

        if created:
            dados_falta.save()

    # Renderiza um template simples de confirmação
    return redirect(request, 'listagemfaltas')


def atualizar_lista_notas(request):
    dados_aluno = Cadastroaluno.objects.all()

    for dado_aluno in dados_aluno:
        dados_nota, created = Notas.objects.get_or_create(
            nomecompleto_nota=dado_aluno.nomecompleto_aluno,
            classe_nota=dado_aluno.classe_aluno,
            datahoje_nota=date.today(),
        )

        if created:
            dados_nota.save()

    return HttpResponse('Lista de notas atualizada com sucesso!')



@csrf_exempt
def salvar_presenca(request):
    if request.method == "POST":
        presencas = request.POST.getlist("presencas[]")
        try:
            for presenca in presencas:
                id_falta, presenca_falta = presenca.split("-")
                aluno_falta = Faltas.objects.get(id_falta=id_falta, datahoje_falta=date.today())
                aluno_falta.presenca_falta = presenca_falta
                aluno_falta.save()
            return JsonResponse({"success": True})
        except Faltas.DoesNotExist:
            return JsonResponse({"success": False, "message": "Falta não encontrada"})
    else:
        return JsonResponse({"success": False, "message": "Método não permitido"})
    


def salvar_notas(request):
    if request.method == 'POST':
        data = json.loads(request.POST['dados'])

        for nota_data in data:
            nota_obj = Notas.objects.get(id_nota=nota_data['id_nota'])
            nota_obj.atividade_nota = nota_data['atividade_nota']
            nota_obj.nota_nota = nota_data['nota_nota']
            nota_obj.save()

        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False, "error": "Invalid request method"})
    
    
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada com sucesso para {username}! Você pode fazer login agora.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'paginas/registro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha inválidos')

    return render(request, 'paginas/login.html')
