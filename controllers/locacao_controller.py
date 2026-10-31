from flask import Blueprint, render_template

locacoes_bp = Blueprint("locacoes", __name__)


@locacoes_bp.route("/locacoes")
def listar_locacoes():
    return render_template("locacoes.html")


@locacoes_bp.route("/locacoes/nova")
def nova_locacao():
    return render_template("locacao_form.html")


@locacoes_bp.route("/locacoes/<int:id>/editar")
def editar_locacao(id):
    return render_template("locacao_form.html")
