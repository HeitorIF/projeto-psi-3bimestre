from flask import Blueprint, render_template, request, redirect, url_for

from database import db
from models import Cliente

clientes_bp = Blueprint("clientes", __name__)


@clientes_bp.route("/clientes")
def listar_clientes():
    clientes = Cliente.query.order_by(Cliente.id.asc()).all()
    return render_template("clientes.html", clientes=clientes)


@clientes_bp.route("/clientes/novo", methods=["GET", "POST"])
def novo_cliente():
    if request.method == "POST":
        cliente = Cliente(
            nome=request.form["nome"],
            cpf=request.form["cpf"],
            email=request.form["email"],
            telefone=request.form["telefone"],
        )
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for("clientes.listar_clientes"))
    return render_template("cliente_form.html", titulo="Novo cliente", cliente=None)


@clientes_bp.route("/clientes/<int:id>/editar", methods=["GET", "POST"])
def editar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    if request.method == "POST":
        cliente.nome = request.form["nome"]
        cliente.cpf = request.form["cpf"]
        cliente.email = request.form["email"]
        cliente.telefone = request.form["telefone"]
        db.session.commit()
        return redirect(url_for("clientes.listar_clientes"))
    return render_template("cliente_form.html", titulo="Editar cliente", cliente=cliente)


@clientes_bp.route("/clientes/<int:id>/excluir", methods=["POST"])
def excluir_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for("clientes.listar_clientes"))
