from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.nome

# Create your models here.
