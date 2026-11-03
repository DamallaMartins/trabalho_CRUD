from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render

from filme.models import FilmeDiretor


def index(request):
    diretores = (
        FilmeDiretor.objects
        .exclude(diretor="")
        .values("diretor")
        .annotate(filmes_count=Count("filme", distinct=True))
        .order_by("diretor")
    )
    return render(request, "diretor/index.html", {"diretores": diretores})