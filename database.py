from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_db():
    from models import Cliente, Jogo, Locacao, LocacaoJogo  # noqa: F401
    db.create_all()
