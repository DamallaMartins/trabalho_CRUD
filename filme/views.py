from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from .models import Filme, FilmePais, FilmeDiretor, FilmeGenero

@login_required
def filme(request):
    todos_filmes = Filme.objects.all()
    filmes = todos_filmes
    busca = request.GET.get('busca', '').strip()

    if busca:
        filmes = filmes.filter(nome__icontains=busca)

    media = todos_filmes.aggregate(media=Avg('nota'))['media'] or 0
    vistos = todos_filmes.filter(assistido=True).count()
    nao_vistos = todos_filmes.filter(assistido=False).count()

    diretores = list(
        FilmeDiretor.objects
        .exclude(diretor='')
        .values('diretor')
        .annotate(total=Count('filme'))
        .order_by('-total')
    )
    diretor_top = diretores[0] if diretores else None

    paises = list(
        FilmePais.objects
        .exclude(pais_origem='')
        .values('pais_origem')
        .annotate(total=Count('filme'))
        .order_by('-total', 'pais_origem')
    )
    pais_top = None
    if paises:
        pais = paises[0]
        nomes_paises = dict(FilmePais._meta.get_field('pais_origem').choices)
        pais_top = {
            'pais': nomes_paises.get(pais['pais_origem'], pais['pais_origem']),
            'total': pais['total'],
        }

    contexto = {
        'filmes': filmes,
        'media_notas': media,
        'vistos': vistos,
        'nao_vistos': nao_vistos,
        'diretor_top': diretor_top,
        'pais_top': pais_top,
        'diretores_labels': [item['diretor'] for item in diretores],
        'diretores_dados': [item['total'] for item in diretores],
    }

    return render(request, 'filme.html', contexto)

@login_required
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

@login_required
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

@login_required
def excluir_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    if request.method == 'POST':
            filme.delete()
            return redirect('filme')
    return render(request, 'aluno/confirmar_exclusao.html', {'filme': filme})