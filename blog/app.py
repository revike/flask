from flask import Flask

from blog import commands
# from blog.admin.views import admin_bp
# from blog.article.views import article
from blog.author.views import author
from blog.extensions import login_manager, db, migrate, csrf, admin_panel
from blog.models_db.models import User

# from blog.user.views import user
from blog.auth.views import auth


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('blog.config')

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    csrf.init_app(app)
    admin_panel.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app: Flask):
    # app.register_blueprint(user)
    # app.register_blueprint(article)
    app.register_blueprint(auth)
    app.register_blueprint(author)
    # app.register_blueprint(admin_bp)


def register_commands(app):
    app.cli.add_command(commands.init_db)
    app.cli.add_command(commands.create_users)
    app.cli.add_command(commands.create_tags)
