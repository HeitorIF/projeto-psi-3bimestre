from app import app
from database import db
from models import Cliente, Jogo, Locacao, LocacaoJogo


def popular_dados():
    with app.app_context():
        db.drop_all()
        db.create_all()

        cliente1 = Cliente(nome="Ana Souza", cpf="123.456.789-00", email="ana@email.com", telefone="(11) 98765-4321")
        cliente2 = Cliente(nome="Bruno Lima", cpf="321.654.987-11", email="bruno@email.com", telefone="(11) 91234-5678")

        jogo1 = Jogo(titulo="The Last of Us", plataforma="PlayStation", genero="Aventura", preco_aluguel=12.0, estoque=4)
        jogo2 = Jogo(titulo="Halo Infinite", plataforma="Xbox", genero="Ação", preco_aluguel=10.0, estoque=3)
        jogo3 = Jogo(titulo="Minecraft", plataforma="PC", genero="Sobrevivência", preco_aluguel=8.5, estoque=6)

        db.session.add_all([cliente1, cliente2, jogo1, jogo2, jogo3])
        db.session.commit()

        locacao1 = Locacao(cliente_id=cliente1.id, data_retirada="2026-10-20", data_devolucao="2026-10-27", status="Em andamento")
        locacao1.jogos.append(jogo1)
        locacao1.jogos.append(jogo3)

        locacao2 = Locacao(cliente_id=cliente2.id, data_retirada="2026-10-22", data_devolucao="2026-10-29", status="Ativa")
        locacao2.jogos.append(jogo2)

        db.session.add_all([locacao1, locacao2])
        db.session.commit()

        print("Dados iniciais carregados com sucesso.")


if __name__ == "__main__":
    popular_dados()
