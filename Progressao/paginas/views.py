from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Cadastroaluno
from .models import Notas
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect


class PaginaInicial(TemplateView):
    template_name= "paginas/index.html"
    
class SobreView(TemplateView):
    template_name="paginas/sobre.html"

class CadastroalunoView(TemplateView):
    template_name="paginas/cadastroaluno.html"
    
class CadastronotaView(TemplateView):
    template_name="paginas/cadastronota.html"
    
class NotasView(TemplateView):
    template_name="paginas/notas.html"

  
def aluno(request):
    if request.method=='POST':
        novo_aluno = Cadastroaluno()
        novo_aluno.nome = request.POST.get('nome')
        novo_aluno.ra = request.POST.get('ra')
        novo_aluno.rg = request.POST.get('rg')
        novo_aluno.datadenascimento = request.POST.get('datadenascimento')
        novo_aluno.save()
    return redirect('/listagemalunos/')

def nota(request):
    if request.method=='POST':
        nova_nota = Notas()
        nova_nota.nome = request.POST.get('nome')
        nova_nota.ra = request.POST.get('ra')
        nova_nota.bimestre1_prova1 = request.POST.get('bimestre1_prova1')
        nova_nota.bimestre1_prova2 = request.POST.get('bimestre1_prova2')
        nova_nota.bimestre1_prova3 = request.POST.get('bimestre1_prova3')
        nova_nota.bimestre2_prova1 = request.POST.get('bimestre2_prova1')
        nova_nota.bimestre2_prova2 = request.POST.get('bimestre2_prova2')
        nova_nota.bimestre2_prova3 = request.POST.get('bimestre2_prova3')
        nova_nota.bimestre3_prova1 = request.POST.get('bimestre3_prova1')
        nova_nota.bimestre3_prova2 = request.POST.get('bimestre3_prova2')
        nova_nota.bimestre3_prova3 = request.POST.get('bimestre3_prova3')
        nova_nota.bimestre4_prova1 = request.POST.get('bimestre4_prova1')
        nova_nota.bimestre4_prova2 = request.POST.get('bimestre4_prova2')
        nova_nota.bimestre4_prova3 = request.POST.get('bimestre4_prova3')
        nova_nota.bimestre5_prova1 = request.POST.get('bimestre5_prova1')
        nova_nota.bimestre5_prova2 = request.POST.get('bimestre5_prova2')
        nova_nota.bimestre5_prova3 = request.POST.get('bimestre5_prova3')
        nova_nota.bimestre6_prova1 = request.POST.get('bimestre6_prova1')
        nova_nota.bimestre6_prova2 = request.POST.get('bimestre6_prova2')
        nova_nota.bimestre6_prova3 = request.POST.get('bimestre6_prova3')
        nova_nota.save()
    return redirect('/listagemnotas/')

class ListagemalunoView(TemplateView):
    template_name = "paginas/listagemalunos.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        alunos = Cadastroaluno.objects.all()
        context["alunos"] = alunos
        return context
    
class ListagemnotaView(TemplateView):
    template_name = "paginas/listagemnotas.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        notas = Notas.objects.all()
        context["notas"] = notas
        return context
    

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

def notas_json(request):
    notas = Notas.objects.all()
    data = []
    for nota in notas:
        data.append({
            'id': nota.id,
            'nome': nota.nome,
            'ra': nota.ra,
            'bimestre1_prova1': nota.bimestre1_prova1,
            'bimestre1_prova2': nota.bimestre1_prova2,
            'bimestre1_prova3': nota.bimestre1_prova3,
            'bimestre2_prova1': nota.bimestre2_prova1,
            'bimestre2_prova2': nota.bimestre2_prova2,
            'bimestre2_prova3': nota.bimestre2_prova3,
            'bimestre3_prova1': nota.bimestre3_prova1,
            'bimestre3_prova2': nota.bimestre3_prova2,
            'bimestre3_prova3': nota.bimestre3_prova3,
            'bimestre4_prova1': nota.bimestre4_prova1,
            'bimestre4_prova2': nota.bimestre4_prova2,
            'bimestre4_prova3': nota.bimestre4_prova3,
            'bimestre5_prova1': nota.bimestre5_prova1,
            'bimestre5_prova2': nota.bimestre5_prova2,
            'bimestre5_prova3': nota.bimestre5_prova3,
            'bimestre6_prova1': nota.bimestre6_prova1,
            'bimestre6_prova2': nota.bimestre6_prova2,
            'bimestre6_prova3': nota.bimestre6_prova3,
        })
    return JsonResponse({'data': data})

def excluir_aluno(request, id_aluno):
    print(aluno)
    aluno = Cadastroaluno.objects.get(id_aluno=id_aluno)
    aluno.delete()
    return redirect('aluno')