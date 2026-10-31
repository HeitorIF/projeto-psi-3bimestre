from flask import Blueprint, render_template

jogos_bp = Blueprint("jogos", __name__)


@jogos_bp.route("/jogos")
def listar_jogos():
    return render_template("jogos.html")


@jogos_bp.route("/jogos/novo")
def novo_jogo():
    return render_template("jogo_form.html")


@jogos_bp.route("/jogos/<int:id>/editar")
def editar_jogo(id):
    return render_template("jogo_form.html")
