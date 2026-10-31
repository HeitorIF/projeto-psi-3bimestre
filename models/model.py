from sqlalchemy.orm import relationship

from database import db


class Cliente(db.Model):
    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=True)
    cpf = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    telefone = db.Column(db.String(30), nullable=True)

    locacoes = relationship("Locacao", back_populates="cliente")


class Jogo(db.Model):
    __tablename__ = "jogo"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=True)
    plataforma = db.Column(db.String(50), nullable=True)
    genero = db.Column(db.String(60), nullable=True)
    preco_aluguel = db.Column(db.Float, nullable=True)
    estoque = db.Column(db.Integer, nullable=True)

    locacoes = relationship("Locacao", secondary="locacao_jogo", back_populates="jogos")


class Locacao(db.Model):
    __tablename__ = "locacao"

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey("cliente.id"), nullable=True)
    data_retirada = db.Column(db.String(20), nullable=True)
    data_devolucao = db.Column(db.String(20), nullable=True)
    status = db.Column(db.String(30), nullable=True)

    cliente = relationship("Cliente", back_populates="locacoes")
    jogos = relationship("Jogo", secondary="locacao_jogo", back_populates="locacoes")


class LocacaoJogo(db.Model):
    __tablename__ = "locacao_jogo"

    locacao_id = db.Column(db.Integer, db.ForeignKey("locacao.id"), primary_key=True)
    jogo_id = db.Column(db.Integer, db.ForeignKey("jogo.id"), primary_key=True)
