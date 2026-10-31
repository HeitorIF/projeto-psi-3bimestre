from flask import Blueprint, render_template, request, redirect, url_for


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("dashboard.dashboard"))
    return render_template("login.html")
