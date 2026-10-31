from sqlalchemy.orm import relationship

from database import db


class Cliente(db.Model):
    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    cpf = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    telefone = db.Column(db.String(30), nullable=False)

    locacoes = relationship("Locacao", back_populates="cliente")

    def __repr__(self):
        return f"Cliente({self.nome})"


class Jogo(db.Model):
    __tablename__ = "jogo"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    plataforma = db.Column(db.String(50), nullable=False)
    genero = db.Column(db.String(60), nullable=False)
    preco_aluguel = db.Column(db.Float, nullable=False)
    estoque = db.Column(db.Integer, nullable=False, default=0)

    locacoes = relationship("Locacao", secondary="locacao_jogo", back_populates="jogos")

    def __repr__(self):
        return f"Jogo({self.titulo})"


class Locacao(db.Model):
    __tablename__ = "locacao"

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey("cliente.id"), nullable=False)
    data_retirada = db.Column(db.String(20), nullable=False)
    data_devolucao = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(30), nullable=False, default="Ativa")

    cliente = relationship("Cliente", back_populates="locacoes")
    jogos = relationship("Jogo", secondary="locacao_jogo", back_populates="locacoes")

    def __repr__(self):
        return f"Locacao({self.id})"


class LocacaoJogo(db.Model):
    __tablename__ = "locacao_jogo"

    locacao_id = db.Column(db.Integer, db.ForeignKey("locacao.id"), primary_key=True)
    jogo_id = db.Column(db.Integer, db.ForeignKey("jogo.id"), primary_key=True)
