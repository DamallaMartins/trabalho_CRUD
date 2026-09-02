from django.shortcuts import render, get_object_or_404, redirect
from .models import Filme

def filme(request):
    filmes = Filme.objects.all()
    return render(request, 'filme.html', {'filmes': filmes})

# Create your views here.
def criar_filme(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        pais_origem = request.POST['pais_origem']
        diretor = request.POST['diretor']
        genero = request.POST['genero']
        review = request.POST.get('review', '')
        nota = request.POST.get('nota') or None
        data_assistido = request.POST.get('data_assistido') or None
        assistido = request.POST.get('assistido') == 'on'
        filme = Filme(
            nome=nome,
            pais_origem=pais_origem,
            diretor=diretor,
            genero=genero,
            review=review,
            nota=nota,
            data_assistido=data_assistido,
            assistido=assistido,
        )
        filme.full_clean()
        filme.save()
        return redirect('filme')
    return render(request, 'aluno/form_filme.html', {'titulo': 'Novo Filme'})

def editar_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    if request.method == 'POST':
        filme.nome = request.POST['nome']
        filme.pais_origem = request.POST['pais_origem']
        filme.diretor = request.POST['diretor']
        filme.genero = request.POST['genero']
        filme.review = request.POST.get('review', '')
        filme.nota = request.POST.get('nota') or None
        filme.data_assistido = request.POST.get('data_assistido') or None
        filme.assistido = request.POST.get('assistido') == 'on'
        filme.full_clean()
        filme.save()
        return redirect('filme')
    return render(request, 'aluno/form_filme.html', {'filme': filme, 'titulo': f'Editar: {filme.nome}'})

def excluir_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    if request.method == 'POST':
            filme.delete()
            return redirect('filme')
    return render(request, 'aluno/confirmar_exclusao.html', {'filme': filme})