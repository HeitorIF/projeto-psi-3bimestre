from flask import Blueprint, render_template

clientes_bp = Blueprint("clientes", __name__)


@clientes_bp.route("/clientes")
def listar_clientes():
    return render_template("clientes.html")


@clientes_bp.route("/clientes/novo")
def novo_cliente():
    return render_template("cliente_form.html")


@clientes_bp.route("/clientes/<int:id>/editar")
def editar_cliente(id):
    return render_template("cliente_form.html")
