from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django_countries.fields import CountryField


class Filme(models.Model):
    nome = models.CharField(max_length=100)
    diretor = models.CharField(max_length=100, default='')
    genero = models.CharField(max_length=100, default='')
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
    pais_origem = CountryField(blank_label="(selecionar país)")

# Create your models here.
