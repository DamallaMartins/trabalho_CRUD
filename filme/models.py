from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django_countries.fields import CountryField


class Filme(models.Model):
    nome = models.CharField(max_length=100)
    review = models.TextField(blank=True)
    nota = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    data_assistido = models.DateField(null=True, blank=True)
    assistido = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class FilmePais(models.Model):
    filme = models.OneToOneField(Filme, on_delete=models.CASCADE, related_name='dados_pais', null=True, blank=True)
    pais_origem = CountryField(blank_label="(selecionar país)")

class FilmeDiretor(models.Model):
    filme = models.OneToOneField(Filme, on_delete=models.CASCADE, related_name='dados_diretor', null=True, blank=True)
    diretor = models.CharField(max_length=100, default='')

class FilmeGenero(models.Model):
    filme = models.OneToOneField(Filme, on_delete=models.CASCADE, related_name='dados_genero', null=True, blank=True)
    genero = models.CharField(max_length=100, default='')

# Create your models here.
