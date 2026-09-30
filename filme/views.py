from django.shortcuts import render, get_object_or_404, redirect
from .models import Filme, FilmePais, FilmeDiretor, FilmeGenero

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
            review=review,
            nota=nota,
            data_assistido=data_assistido,
            assistido=assistido,
        )
        filme.full_clean()
        filme.save()
        dados_pais = FilmePais(filme=filme, pais_origem=pais_origem)
        dados_diretor = FilmeDiretor(filme=filme, diretor=diretor)
        dados_genero = FilmeGenero(filme=filme, genero=genero)
        dados_pais.full_clean()
        dados_diretor.full_clean()
        dados_genero.full_clean()
        dados_pais.save()
        dados_diretor.save()
        dados_genero.save()
        return redirect('filme')
    paises = FilmePais._meta.get_field('pais_origem').choices
    return render(request, 'aluno/form_filme.html', {'titulo': 'Novo Filme', 'paises': paises})

def editar_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    if request.method == 'POST':
        filme.nome = request.POST['nome']
        filme.review = request.POST.get('review', '')
        filme.nota = request.POST.get('nota') or None
        filme.data_assistido = request.POST.get('data_assistido') or None
        filme.assistido = request.POST.get('assistido') == 'on'
        filme.full_clean()
        filme.save()
        dados_pais, _ = FilmePais.objects.get_or_create(filme=filme)
        dados_diretor, _ = FilmeDiretor.objects.get_or_create(filme=filme)
        dados_genero, _ = FilmeGenero.objects.get_or_create(filme=filme)
        dados_pais.pais_origem = request.POST['pais_origem']
        dados_diretor.diretor = request.POST['diretor']
        dados_genero.genero = request.POST['genero']
        dados_pais.full_clean()
        dados_diretor.full_clean()
        dados_genero.full_clean()
        dados_pais.save()
        dados_diretor.save()
        dados_genero.save()
        return redirect('filme')
    paises = FilmePais._meta.get_field('pais_origem').choices
    return render(request, 'aluno/form_filme.html', {
        'filme': filme,
        'titulo': f'Editar: {filme.nome}',
        'paises': paises,
    })

def excluir_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    if request.method == 'POST':
            filme.delete()
            return redirect('filme')
    return render(request, 'aluno/confirmar_exclusao.html', {'filme': filme})