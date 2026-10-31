from flask import Blueprint, render_template

from models import Cliente, Jogo, Locacao


dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
def dashboard():
    return render_template(
        "dashboard.html",
        total_clientes=Cliente.query.count(),
        total_jogos=Jogo.query.count(),
        total_locacoes=Locacao.query.count(),
    )
