from django.test import TestCase
from django.urls import reverse

from .models import Filme, FilmeDiretor, FilmeGenero, FilmePais


class FilmeCrudTests(TestCase):
	def payload(self, **overrides):
		data = {
			'nome': 'Central do Brasil',
			'pais_origem': 'BR',
			'diretor': 'Walter Salles',
			'genero': 'Drama',
			'review': 'Um filme brasileiro.',
			'nota': '5',
			'data_assistido': '',
		}
		data.update(overrides)
		return data

	def test_create_saves_dedicated_models(self):
		response = self.client.post(reverse('criar_filme'), self.payload())

		self.assertRedirects(response, reverse('filme'))
		filme = Filme.objects.get(nome='Central do Brasil')
		self.assertEqual(filme.dados_pais.pais_origem, 'BR')
		self.assertEqual(filme.dados_diretor.diretor, 'Walter Salles')
		self.assertEqual(filme.dados_genero.genero, 'Drama')

	def test_edit_updates_dedicated_models(self):
		filme = Filme.objects.create(nome='Filme antigo')
		FilmePais.objects.create(filme=filme, pais_origem='BR')
		FilmeDiretor.objects.create(filme=filme, diretor='Diretor antigo')
		FilmeGenero.objects.create(filme=filme, genero='Gênero antigo')

		response = self.client.post(
			reverse('editar_filme', args=[filme.pk]),
			self.payload(nome='Filme atualizado', pais_origem='US'),
		)

		self.assertRedirects(response, reverse('filme'))
		filme.refresh_from_db()
		self.assertEqual(filme.nome, 'Filme atualizado')
		self.assertEqual(filme.dados_pais.pais_origem, 'US')
		self.assertEqual(filme.dados_diretor.diretor, 'Walter Salles')
		self.assertEqual(filme.dados_genero.genero, 'Drama')
