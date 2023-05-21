from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cadastroaluno, Cadastroprofessor, Notas, Faltas
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from datetime import date
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib import messages


def in_professores_group(user):
    return 'Professores' in [group.name for group in user.groups.all()]

def in_secretaria_group(user):
    return 'Secretaria' in [group.name for group in user.groups.all()]

@login_required
def pagina_inicial(request):
    return render(request, 'paginas/index.html')

@login_required
def sobre(request):
    return render(request, 'paginas/sobre.html')

@login_required
@user_passes_test(in_secretaria_group)
def cadastro_aluno(request):
    return render(request, 'paginas/cadastroaluno.html')

@login_required
@user_passes_test(in_secretaria_group)
def cadastro_professor(request):
    return render(request, 'paginas/cadastroprofessor.html')

@login_required
@user_passes_test(in_professores_group)
def cadastro_nota(request):
    return render(request, 'paginas/cadastronota.html')

@login_required
@user_passes_test(in_professores_group)
def cadastro_falta(request):
    return render(request, 'paginas/cadastrofalta.html')

@login_required
@user_passes_test(in_professores_group)
def notas(request):
    return render(request, 'paginas/notas.html')

@login_required
@user_passes_test(in_professores_group)
def area_professor(request):
    return render(request, 'paginas/areadoprofessor.html')

@login_required
@user_passes_test(in_secretaria_group)
def area_secretaria(request):
    return render(request, 'paginas/areadasecretaria.html')

@login_required
@user_passes_test(in_secretaria_group)
def area_aluno(request):
    return render(request, 'paginas/areadoaluno.html')

@login_required
@user_passes_test(in_secretaria_group)
def cadastro_turma(request):
    return render(request, 'paginas/cadastroturma.html')

@login_required
@user_passes_test(in_secretaria_group)
def selecaoturma(request):
    alunos = Cadastroaluno.objects.all()
    context = {'alunos': alunos}
    return render(request, 'selecaoturma.html', context)

@login_required
@user_passes_test(in_professores_group)
@user_passes_test(in_secretaria_group)
def aluno(request):
    if request.method=='POST':
        novo_aluno = Cadastroaluno()
        novo_aluno.nome = request.POST.get('nome')
        novo_aluno.ra = request.POST.get('ra')
        novo_aluno.rg = request.POST.get('rg')
        novo_aluno.datadenascimento = request.POST.get('datadenascimento')
        novo_aluno.save()
    return redirect('/listagemalunos/')


#def alunos_json(request):
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

@login_required
@user_passes_test(in_secretaria_group)
def listagem_alunos(request):
    template_name = "paginas/listagemalunos.html"
    alunos = Cadastroaluno.objects.all()
    context = {"alunos": alunos}
    return render(request, template_name, context)

@login_required
def listagem_turma_professor(request):
    template_name = "paginas/listagemturmaprofessor.html"
    alunos = Cadastroprofessor.objects.all()
    context = {"alunos": alunos}
    return render(request, template_name, context)

@login_required
@user_passes_test(in_secretaria_group)
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

@login_required
@user_passes_test(in_professores_group)
def listagem_notas(request):
    template_name = "paginas/listagemnotas.html"
    notas = Notas.objects.all()
    context = {"notas": notas}
    return render(request, template_name, context)

@login_required
@user_passes_test(in_professores_group)
def listagem_faltas(request):
    template_name = "paginas/listagemfaltas.html"
    faltas = Faltas.objects.all()
    context = {"faltas": faltas}
    return render(request, template_name, context)

@login_required
@user_passes_test(in_secretaria_group)
def listagem_turmas(request):
    template_name = "paginas/listagemturmas.html"
    turmas = Cadastroaluno.objects.all()
    context = {"turma": turmas}
    return render(request, template_name, context)

@login_required
@user_passes_test(in_secretaria_group)
@user_passes_test(in_professores_group)
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

@login_required
@user_passes_test(in_secretaria_group)
@user_passes_test(in_professores_group)
def cadastrar_faltas(request):
    if request.method == 'POST':
        cpf_faltas = request.POST['cpf_faltas']
        data_faltas = request.POST['data_faltas']
        presenca_faltas = request.POST['presenca_faltas']
        faltas = Faltas(cpf_faltas=cpf_faltas, data_faltas=data_faltas, presenca_faltas=presenca_faltas)
        print(cpf_faltas, data_faltas, presenca_faltas)
        faltas.save()
        return redirect('/cadastrofalta/')

@login_required
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

@login_required
@user_passes_test(in_secretaria_group)
def cadastrar_professores(request):
    if request.method == 'POST':
        # Cria o usuário
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password != password2:
            # Senhas não combinam
            return HttpResponse("Senhas não combinam")

        user = User.objects.create_user(username=username, password=password)
        user.save()

        # Determine o grupo com base no prefixo do username
        if username.startswith("sc-"):
            group_name = 'Secretaria'
        elif username.startswith("pf-"):
            group_name = 'Professores'
        else:
            return HttpResponse("Nome de usuário inválido. Deve começar com 'sc-' para Secretaria ou 'pf-' para Professores.")

        # Cria o grupo se necessário e adiciona o usuário a ele
        group, created = Group.objects.get_or_create(name=group_name)
        group.user_set.add(user)

        # Cria o registro do professor
        professor = Cadastroprofessor(
            user=user,
            cpf_professor=request.POST['cpf_professor'],
            nomecompleto_professor=request.POST['nomecompleto_professor'],
            datadenascimento_professor=request.POST['datadenascimento_professor'],
            rua_professor=request.POST['rua_professor'],
            numero_professor=request.POST['numero_professor'],
            bairro_professor=request.POST['bairro_professor'],
            municipio_professor=request.POST['municipio_professor'],
            formacao_professor=request.POST['formacao_professor'],
            email_professor=request.POST['email_professor'],
            # classe_professor=request.POST['classe_professor'], # Adicione este campo ao formulário se necessário
        )
        professor.save()

        return redirect('login')
    else:
        return render(request, 'paginas/cadastrar_professores.html')


@login_required
@user_passes_test(in_professores_group)
def notas_json(request):
    hoje = date.today()
    professor = Cadastroprofessor.objects.get(user=request.user)
    notas = Notas.objects.filter(datahoje_nota=hoje, classe_nota=professor.classe_professor)
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



@login_required
@user_passes_test(in_professores_group)
def faltas_json(request):
    hoje = date.today()
    professor = Cadastroprofessor.objects.get(user=request.user)
    faltas = Faltas.objects.filter(datahoje_falta=hoje, classe_falta=professor.classe_professor)
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



@login_required
@user_passes_test(in_secretaria_group)
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

@login_required
@user_passes_test(in_secretaria_group)
@user_passes_test(in_professores_group)
def excluir_aluno(request, id_aluno):
    aluno = get_object_or_404(Cadastroaluno, id_aluno=id_aluno)
    aluno.delete()
    return redirect('listagemalunos')

@login_required
@user_passes_test(in_professores_group)
def excluir_nota(request, id_notas):
    nota = get_object_or_404(Notas, id_notas=id_notas)
    nota.delete()
    return redirect('listagemnotas')

@login_required
@user_passes_test(in_secretaria_group)
@user_passes_test(in_professores_group)
def excluir_falta(request, id_faltas):
    falta = get_object_or_404(Faltas, id_faltas=id_faltas)
    falta.delete()
    return redirect('listagemfaltas')


#Busca os dados do Cadastro aluno para aparecer na página de cadastro de turmas 
@login_required
@user_passes_test(in_secretaria_group)
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

@login_required
def turmasprofessor_json(request):
    professores = Cadastroprofessor.objects.all()
    data = {'data': []}
    for professor in professores:
        data['data'].append({
            'id_professor': professor.id_professor,
            'cpf_professor': professor.cpf_professor,
            'nomecompleto_professor': professor.nomecompleto_professor,
            'classe_professor': professor.classe_professor,
            'bairro_professor': professor.bairro_professor
        })
    return JsonResponse(data)


#Salva o dado no banco em Classe
@login_required
@user_passes_test(in_secretaria_group)
def associar_aluno(request, id_aluno):
    classe = request.POST['classe_turma']
    print(classe)
    aluno = Cadastroaluno.objects.get(pk=id_aluno)
    aluno.classe_aluno = classe
    aluno.save()
    return redirect('listagemturmas')

@login_required
@user_passes_test(in_secretaria_group)
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
    return HttpResponse('Lista de notas atualizada com sucesso!')

@login_required
@user_passes_test(in_secretaria_group)
@user_passes_test(in_professores_group)
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


@login_required
@user_passes_test(in_secretaria_group)
@user_passes_test(in_professores_group)
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
    

@login_required
@user_passes_test(in_secretaria_group)
@user_passes_test(in_professores_group)
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
    
@login_required
@user_passes_test(in_secretaria_group)
@user_passes_test(in_professores_group)
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

@login_required
@user_passes_test(in_secretaria_group)
@user_passes_test(in_professores_group)
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

@login_required
def selecionar_turma(request, id_professor):
    classe = request.POST['classe_professor']
    professor = Cadastroprofessor.objects.get(pk=id_professor)
    professor.classe_professor = classe
    professor.save()
    return redirect('listagemturmaprofessor')

@login_required
@user_passes_test(in_secretaria_group)
@user_passes_test(in_professores_group)
class ProfessorRegistrationForm(UserCreationForm):
    cpf_professor = forms.CharField(max_length=11, required=True)
    nomecompleto_professor = forms.CharField(max_length=100, required=True)
    datadenascimento_professor = forms.DateField(required=True)
    rua_professor = forms.CharField(max_length=100, required=True)
    numero_professor = forms.CharField(max_length=100, required=True)
    bairro_professor = forms.CharField(max_length=100, required=True)
    municipio_professor = forms.CharField(max_length=100, required=True)
    formacao_professor = forms.CharField(max_length=100, required=True)
    email_professor = forms.EmailField(max_length=254, required=True)
    classe_professor = forms.ChoiceField(choices=Cadastroprofessor.classe_choices_professor, required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'cpf_professor', 'nomecompleto_professor', 'datadenascimento_professor', 'rua_professor', 'numero_professor', 'bairro_professor', 'municipio_professor', 'formacao_professor', 'email_professor', 'classe_professor']

@login_required
@user_passes_test(in_secretaria_group)
@user_passes_test(in_professores_group)
def register_professor(request):
    if request.method == 'POST':
        form = ProfessorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Aqui estava o problema
            group, created = Group.objects.get_or_create(name='Professores')
            group.user_set.add(user)

            professor = Cadastroprofessor(
                user=user,
                cpf_professor=form.cleaned_data.get('cpf_professor'),
                nomecompleto_professor=form.cleaned_data.get('nomecompleto_professor'),
                datadenascimento_professor=form.cleaned_data.get('datadenascimento_professor'),
                rua_professor=form.cleaned_data.get('rua_professor'),
                numero_professor=form.cleaned_data.get('numero_professor'),
                bairro_professor=form.cleaned_data.get('bairro_professor'),
                municipio_professor=form.cleaned_data.get('municipio_professor'),
                formacao_professor=form.cleaned_data.get('formacao_professor'),
                email_professor=form.cleaned_data.get('email_professor'),
                classe_professor=form.cleaned_data.get('classe_professor'),
            )

            professor.save()

            messages.success(request, f'Conta de professor criada com sucesso para {form.cleaned_data.get("username")}! Você pode fazer login agora.')
            return redirect('login')
    else:
        form = ProfessorRegistrationForm()
    return render(request, 'paginas/registro.html', {'form': form})


