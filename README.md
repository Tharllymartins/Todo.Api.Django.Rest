# Lista de Tarefas - Projeto Django com DRF
Este é um projeto de lista de tarefas desenvolvido com o framework Django e a API foi criada com o Django Rest Framework (DRF). O projeto usa o Poetry para gerenciar as dependências.

## Pré-requisitos

- Python 3.x

- Poetry

## Passos para execução local
- Clone o repositório com o comando git clone https://github.com/Tharllymartins/Todo.Api.Django.Rest.git
- Entre na pasta do projeto com o comando cd Todo.Api.Django.Rest
- Instale as dependências com o comando poetry install
- Rode as migrações com o comando python manage.py migrate
- Inicie o servidor local com o comando python manage.py runserver
- Agora, você pode acessar a API na URL http://127.0.0.1:8000/tasks/ e interagir com as tarefas usando os métodos HTTP (GET, POST, PUT, PATCH e DELETE).