# imobiliaria-web - Centralizador de Imóveis - Projeto Integrador UNIVESP
Projeto que gerencia imóveis para locação e venda com redirecionamento para imobiliárias

Este projeto foi desenvolvido como parte do Projeto Integrador Semestral da UNIVESP, com o objetivo de criar uma plataforma web para centralizar imóveis de locação e venda, facilitando a busca pela população e agilizando o fechamento de negócios pelas imobiliárias.

Tecnologias Utilizadas
Frontend: HTML, CSS, JavaScript, Bootstrap
Backend: Python, Django
Banco de Dados: SQLite (pode ser configurado para PostgreSQL ou outro banco de dados relacional)
Gerenciamento de dependências: pip e virtualenv
Metodologia de Desenvolvimento: SCRUM, com reuniões semanais
Requisitos
Antes de começar, certifique-se de ter as seguintes ferramentas instaladas:

Python 3.10+: Instalar Python
Git: Instalar Git
Virtualenv (opcional, mas recomendado): Documentação do virtualenv

Instalação
Siga os passos abaixo para configurar o ambiente localmente:

1. Clone o repositório - git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
2. Crie e ative um ambiente virtual - # Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# No Windows:
venv\Scripts\activate

# No Mac/Linux:
source venv/bin/activate

3. Instale as dependências -
pip install -r requirements.txt

4.Configuração do ambiente

Crie um arquivo .env na raiz do projeto com as variáveis de ambiente necessárias. Um exemplo de configuração pode ser encontrado no arquivo .env.example.

Exemplo de conteúdo do arquivo .env:

DEBUG=True
SECRET_KEY=sua_chave_secreta
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
AWS_ACCESS_KEY_ID=sua_chave_de_acesso
AWS_SECRET_ACCESS_KEY=sua_chave_secreta

5. Execute as migrações do banco de dados

 python manage.py migrate

6. Crie um superusuário - Para acessar a área administrativa do Django, você precisará de um superusuário. Execute o comando abaixo e siga as instruções:

python manage.py createsuperuser

7. Inicie o servidor de desenvolvimento

python manage.py runserver

Agora você pode acessar o projeto em http://127.0.0.1:8000/

Contribuições
Ficamos felizes com contribuições! Se você tiver sugestões ou encontrar bugs, fique à vontade para abrir uma issue ou enviar um pull request.

Passos para Contribuir:
Faça um fork do projeto.
Crie um branch para sua feature (git checkout -b feature/nova-feature).
Commit suas mudanças (git commit -m 'Adiciona nova feature').
Envie para o branch (git push origin feature/nova-feature).
Abra um pull request.
Licença
Este projeto está licenciado sob a licença MIT - consulte o arquivo LICENSE para mais detalhes.



 
  
# Integrantes do Projeto
Rogério Gelonezi - https://www.linkedin.com/in/rogeriogelonezi/

Leonardo Silva - https://www.linkedin.com/in/leonardo16silva12/

Mauro Leão -  https://www.linkedin.com/in/mauro-s%C3%A9rgio-bouwman-le%C3%A3o-b62b41260/
