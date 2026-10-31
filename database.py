from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_db():
    from models import Cliente, Jogo, Locacao, LocacaoJogo
    db.create_all()
