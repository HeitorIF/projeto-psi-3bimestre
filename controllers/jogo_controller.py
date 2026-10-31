from flask import Blueprint, render_template, request, redirect, url_for

from database import db
from models import Jogo

jogos_bp = Blueprint("jogos", __name__)


@jogos_bp.route("/jogos")
def listar_jogos():
    jogos = Jogo.query.order_by(Jogo.id.asc()).all()
    return render_template("jogos.html", jogos=jogos)


@jogos_bp.route("/jogos/novo", methods=["GET", "POST"])
def novo_jogo():
    if request.method == "POST":
        jogo = Jogo(
            titulo=request.form["titulo"],
            plataforma=request.form["plataforma"],
            genero=request.form["genero"],
            preco_aluguel=float(request.form["preco_aluguel"]),
            estoque=int(request.form["estoque"]),
        )
        db.session.add(jogo)
        db.session.commit()
        return redirect(url_for("jogos.listar_jogos"))
    return render_template("jogo_form.html", titulo="Novo jogo", jogo=None)


@jogos_bp.route("/jogos/<int:id>/editar", methods=["GET", "POST"])
def editar_jogo(id):
    jogo = Jogo.query.get_or_404(id)
    if request.method == "POST":
        jogo.titulo = request.form["titulo"]
        jogo.plataforma = request.form["plataforma"]
        jogo.genero = request.form["genero"]
        jogo.preco_aluguel = float(request.form["preco_aluguel"])
        jogo.estoque = int(request.form["estoque"])
        db.session.commit()
        return redirect(url_for("jogos.listar_jogos"))
    return render_template("jogo_form.html", titulo="Editar jogo", jogo=jogo)


@jogos_bp.route("/jogos/<int:id>/excluir", methods=["POST"])
def excluir_jogo(id):
    jogo = Jogo.query.get_or_404(id)
    db.session.delete(jogo)
    db.session.commit()
    return redirect(url_for("jogos.listar_jogos"))
