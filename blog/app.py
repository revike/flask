from flask import Flask, redirect, url_for
from flask_login import LoginManager

from blog.article.views import article
from blog.auth.views import auth
from blog.models.database import db
from blog.models.user import User
from blog.report.views import report
from blog.user.views import user

# login_manager = LoginManager()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '^1*kronpwhp8z5%jy!-!$6igm^8xbge%8+-d_sr1@3@+a4q5d5'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    db.init_app(app)

    login_manager = LoginManager(app)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter_by(id=user_id).one_or_none()

    @login_manager.unauthorized_handler
    def unauthorized():
        return redirect(url_for("auth.login"))

    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(report)
    app.register_blueprint(article)
    app.register_blueprint(auth)
