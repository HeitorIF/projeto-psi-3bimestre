from flask import Flask, redirect, url_for

from controllers import register_blueprints
from database import db, init_db


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "psi-locadora-base"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///locadora.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        init_db()

    register_blueprints(app)

    @app.route("/")
    def index():
        return redirect(url_for("auth.login"))

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
