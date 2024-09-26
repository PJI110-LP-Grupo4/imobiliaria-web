# Imobiliaria-web - Centralizador de Imóveis - Projeto Integrador UNIVESP

Projeto que gerencia imóveis para locação e venda com redirecionamento para imobiliárias.

Este projeto foi desenvolvido como parte do **Projeto Integrador Semestral da UNIVESP**, com o objetivo de criar uma plataforma web para centralizar imóveis de locação e venda, facilitando a busca pela população e agilizando o fechamento de negócios pelas imobiliárias.

## Tecnologias Utilizadas

- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Python, Django
- **Banco de Dados**: SQLite (pode ser configurado para PostgreSQL ou outro banco de dados relacional)
- **Gerenciamento de dependências**: `pip` e `virtualenv`
- **Metodologia de Desenvolvimento**: SCRUM, com reuniões semanais

## Requisitos

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas:

- **Python 3.10+**: [Instalar Python](https://www.python.org/downloads/)
- **Git**: [Instalar Git](https://git-scm.com/)
- **Virtualenv** (opcional, mas recomendado): [Documentação do virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)

## Instalação

Siga os passos abaixo para configurar o ambiente localmente:

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio

# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# No Windows:
venv\Scripts\activate

# No Mac/Linux:
source venv/bin/activate
```
3. Instale as dependências
```bash

pip install -r requirements.txt
```
4. Configuração do ambiente
Crie um arquivo .env na raiz do projeto com as variáveis de ambiente necessárias. Um exemplo de configuração pode ser encontrado no arquivo .env.example.

Exemplo de conteúdo do arquivo .env:
```bash
DEBUG=True
SECRET_KEY=sua_chave_secreta
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
AWS_ACCESS_KEY_ID=sua_chave_de_acesso
AWS_SECRET_ACCESS_KEY=sua_chave_secreta
```
5. Execute as migrações do banco de dados
```bash
python manage.py migrate
```
6. Crie um superusuário
Para acessar a área administrativa do Django, você precisará de um superusuário. Execute o comando abaixo e siga as instruções:

```bash
python manage.py createsuperuser

```
Agora você pode acessar o projeto em http://127.0.0.1:8000/.

7. Inicie o servidor de desenvolvimento
python manage.py runserver

Passos para Contribuir:
Faça um fork do projeto.
Crie um branch para sua feature. ```bash git checkout -b feature/nova-feature```
Commit suas mudanças .```bash git commit -m 'Adiciona nova feature```
Envie para o branch .```bash git push origin feature/nova-feature```
Abra um pull request.

Licença
Este projeto está licenciado sob a licença MIT - consulte o arquivo LICENSE para mais detalhes.

Integrantes do Projeto
Rogério Gelonezi - LinkedIn
Leonardo Silva - LinkedIn
Mauro Leão - LinkedIn


