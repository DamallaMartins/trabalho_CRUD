# Catálogo de filmes

## Equipe

Carlos Eduardo e Dâmalla

## Sobre o projeto

Aplicação web para cadastrar, consultar, editar e excluir filmes. O catálogo permite registrar filmes já assistidos e filmes que ainda estão na lista do usuário para assistir no futuro.

## Progresso do trabalho

- Configuração inicial da aplicação Django e preparação do projeto.
- Implementação do CRUD de filmes.
- Criação dos models para país, diretor e gênero.
- Integração com `django-countries` para seleção de países.
- Adição da página de login e da seção de diretores.
- Implementação das barras de pesquisa para filmes e diretores.
- Criação de pop-ups para visualizar os filmes de um diretor e os detalhes completos de um filme.
- Atualização da tabela de filmes para mostrar somente nome, país de origem, diretor e gênero.
- Atualização do layout, das cores, dos espaçamentos e da responsividade do site.
- Atualização contínua da documentação e das informações do projeto.

## Funcionalidades

- Cadastro, edição e exclusão de filmes.
- Cadastro de país de origem, diretor, gênero e review.
- Pesquisa de filmes pelo nome.
- Pesquisa de diretores pelo nome.
- Visualização dos filmes realizados por um diretor em uma janela pop-up.
- Visualização dos detalhes adicionais de um filme ao clicar em seu nome.
- Exibição da lista de filmes com nome, país de origem, diretor e gênero.
- Exibição de review, nota, data assistida e situação de visualização somente dentro do pop-up do filme.

### Pesquisa

Na página de filmes, digite parte do nome e clique em **Pesquisar**. A barra filtra somente pelo campo `nome`; campos como diretor, gênero ou review não participam dessa pesquisa. Clique em **Limpar** para voltar à lista completa.

Na página de diretores, digite parte do nome do diretor e clique em **Pesquisar**. Clique em **Limpar** para remover o filtro.

### Pop-ups de detalhes

- Em **Diretores**, clique em **Ver filmes** para abrir uma janela contendo os filmes do diretor e seus gêneros.
- Em **Filmes**, clique no nome de um filme para abrir uma janela contendo review, nota, data assistida e se o filme foi assistido.
- Use o botão **Fechar**, no final da janela, para fechá-la.

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
