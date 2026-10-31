from flask import Blueprint, render_template, request, redirect, url_for

from database import db
from models import Cliente, Locacao

locacoes_bp = Blueprint("locacoes", __name__)


@locacoes_bp.route("/locacoes")
def listar_locacoes():
    locacoes = Locacao.query.order_by(Locacao.id.asc()).all()
    return render_template("locacoes.html", locacoes=locacoes)


@locacoes_bp.route("/locacoes/nova", methods=["GET", "POST"])
def nova_locacao():
    clientes = Cliente.query.order_by(Cliente.nome.asc()).all()
    if request.method == "POST":
        locacao = Locacao(
            cliente_id=request.form["cliente_id"],
            data_retirada=request.form["data_retirada"],
            data_devolucao=request.form["data_devolucao"],
            status=request.form["status"],
        )
        db.session.add(locacao)
        db.session.commit()
        return redirect(url_for("locacoes.listar_locacoes"))
    return render_template("locacao_form.html", titulo="Nova locação", locacao=None, clientes=clientes)


@locacoes_bp.route("/locacoes/<int:id>/editar", methods=["GET", "POST"])
def editar_locacao(id):
    clientes = Cliente.query.order_by(Cliente.nome.asc()).all()
    locacao = Locacao.query.get_or_404(id)
    if request.method == "POST":
        locacao.cliente_id = request.form["cliente_id"]
        locacao.data_retirada = request.form["data_retirada"]
        locacao.data_devolucao = request.form["data_devolucao"]
        locacao.status = request.form["status"]
        db.session.commit()
        return redirect(url_for("locacoes.listar_locacoes"))
    return render_template("locacao_form.html", titulo="Editar locação", locacao=locacao, clientes=clientes)


@locacoes_bp.route("/locacoes/<int:id>/excluir", methods=["POST"])
def excluir_locacao(id):
    locacao = Locacao.query.get_or_404(id)
    db.session.delete(locacao)
    db.session.commit()
    return redirect(url_for("locacoes.listar_locacoes"))
