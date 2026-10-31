# Sistema de Locadora de Jogos

## Tema
Sistema web para gerenciamento de uma locadora de jogos físicos e digitais.

## Integrantes
- André Nícolas de Oliveira Santos
- Heitor Emanuel Cavalcanti
- Pedro Henrique Oliveira de Araújo
- Isaac da Costa Barbosa

## Descrição do sistema
A aplicação permite cadastrar clientes, jogos e locações, além de controlar o relacionamento entre clientes e pedidos de aluguel, bem como os itens vinculados a cada locação.

## Entidades principais
- Cliente
- Jogo
- Locacao

## Relacionamentos
- 1:N: um cliente pode ter várias locações.
- N:N: uma locação pode conter vários jogos e um jogo pode estar em várias locações.

## Requisitos
- Python
- Flask
- Flask-SQLAlchemy
- SQLite

## Instalação
1. Crie um ambiente virtual.
2. Instale as dependências:
   `pip install -r requirements.txt`
3. Popule o banco com dados iniciais:
   `python seed.py`
4. Inicie a aplicação:
   `python app.py`
5. Acesse:
   - `http://localhost:5000/` → redireciona para a tela de login
   - `http://localhost:5000/login`
   - `http://localhost:5000/dashboard`

## Funcionalidades finais
- Login inicial com fluxo simples e redirecionamento para o dashboard.
- CRUD completo de clientes.
- CRUD completo de jogos.
- CRUD completo de locações.
- Relacionamento N:N entre locações e jogos.
- Dashboard com contagem geral do sistema.

## Declaração de autoria
Declaro que compreendo o projeto e sou capaz de explicar e alterar suas partes principais.
