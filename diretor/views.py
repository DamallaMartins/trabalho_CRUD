from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render

from filme.models import Filme, FilmeDiretor


def index(request):
    diretores = (
        FilmeDiretor.objects
        .exclude(diretor="")
        .values("diretor")
        .annotate(filmes_count=Count("filme", distinct=True))
        .order_by("diretor")
    )

    busca = request.GET.get("busca", "").strip()
    if busca:
        diretores = diretores.filter(diretor__icontains=busca)

    diretores = list(diretores)
    for diretor in diretores:
        filmes = Filme.objects.filter(
            dados_diretor__diretor__iexact=diretor["diretor"]
        ).order_by("nome")

        diretor["filmes"] = [
            {
                "nome": filme.nome,
                "genero": getattr(
                    getattr(filme, "dados_genero", None),
                    "genero",
                    "",
                ),
            }
            for filme in filmes
        ]

    return render(request, "diretor/index.html", {"diretores": diretores})