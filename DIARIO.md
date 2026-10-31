Data: 10/10 - Heitor
O que foi feito: Definição do tema e estrutura inicial do projeto.
Dificuldade encontrada: Decidir o tema e os relacionamentos entre as entidades.
Como resolvi: Foi escolhido o tema de locadora de jogos com clientes, jogos e locações.
Próximo passo: Estruturar a aplicação em MVC e criar a base dos modelos.

Data: 11/10 - André
O que foi feito: Criação do esqueleto do Flask e organização das pastas do MVC.
Dificuldade encontrada: Separar responsabilidades entre modelo, controller e template.
Como resolvi: A aplicação foi organizada em arquivos específicos para banco, modelos e rotas.
Próximo passo: Implementar o login e as telas iniciais do sistema.

Data: 14/10 - Heitor
O que foi feito: Criação da rota de login e do dashboard inicial, além da navegação entre as telas principais.
Dificuldade encontrada: Dar início ao fluxo do sistema sem misturar a lógica de autenticação com a renderização das páginas.
Como resolvi: Separei a rota de autenticação em um blueprint e deixei o dashboard com o acesso simples aos dados gerais do sistema.
Próximo passo: Trabalhar no cadastro de clientes e na persistência no banco.

Data: 17/10 - André
O que foi feito: Definição dos modelos de Cliente, Jogo e Locacao e da relação entre eles.
Dificuldade encontrada: Organizar corretamente o relacionamento 1:N e o relacionamento N:N sem quebrar a persistência.
Como resolvi: Estruturei as classes com SQLAlchemy, adicionei a tabela intermediária e configurei os relationship necessários para o banco.
Próximo passo: Iniciar o CRUD de clientes e validar a criação dos registros no banco.

Data: 18/10 - Heitor
O que foi feito: Implementação do CRUD de clientes, incluindo cadastro, listagem, edição e exclusão.
Dificuldade encontrada: Conectar o formulário com a persistência no banco e garantir a atualização correta da tabela.
Como resolvi: Criei as rotas do blueprint, renderizei os templates de formulário e listagem e validei o fluxo de criação e remoção no banco.
Próximo passo: Avançar para o módulo de jogos e completar a parte de cadastro do catálogo.
