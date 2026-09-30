# Catálogo de filmes

## Equipe

Carlos Eduardo e Dâmalla

## Sobre o projeto

Aplicação web para cadastrar, consultar, editar e excluir filmes. O catálogo permite registrar filmes já assistidos e filmes que ainda estão na lista do usuário para assistir no futuro.

## Models

O model `Filme` guarda `nome`, `review` (opcional), `nota` (opcional, de 1 a 5), `data_assistido` (opcional) e `assistido` (padrão `False`).

Os dados complementares ficam em models próprios, cada um relacionado a `Filme`:

- `FilmePais`: país de origem.
- `FilmeDiretor`: nome do diretor.
- `FilmeGenero`: gênero do filme.

## Tecnologias utilizadas

- Python 3.11 ou superior
- Django 5.2.17
- SQLite
- HTML5
- CSS3
- Templates do Django

As dependências Python utilizadas estão registradas em `requirements.txt`.

## Como executar

### 1. Pré-requisitos

Tenha o Python instalado e disponível no PATH do sistema.

### 2. Criar e ativar o ambiente virtual

No PowerShell, dentro da pasta do projeto:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Caso o PowerShell bloqueie a ativação, execute uma vez:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Depois, ative o ambiente novamente:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Aplicar as migrations

```powershell
python manage.py migrate
```

### 5. Iniciar o servidor

```powershell
python manage.py runserver
```

Acesse a aplicação em <http://127.0.0.1:8000/>.

## Comandos úteis

Verificar problemas na configuração:

```powershell
python manage.py check
```

Executar os testes:

```powershell
python manage.py test
```

Criar uma nova migration depois de alterar o model:

```powershell
python manage.py makemigrations
python manage.py migrate
```
