from .auth_controller import auth_bp
from .cliente_controller import clientes_bp
from .dashboard_controller import dashboard_bp
from .jogo_controller import jogos_bp
from .locacao_controller import locacoes_bp


def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(clientes_bp)
    app.register_blueprint(jogos_bp)
    app.register_blueprint(locacoes_bp)
