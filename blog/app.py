from flask import Flask
from flask_combo_jsonapi import Api

from blog import commands
from blog.api.article import ArticleList, ArticleDetail
from blog.api.author import AuthorList, AuthorDetail
from blog.api.tag import TagList, TagDetail
from blog.api.user import UserList, UserDetail
from blog.extensions import login_manager, db, migrate, csrf, admin_panel, \
    create_api_spec_plugin
from blog.models_db.models import User


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('blog.config')

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_api(app)

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


def register_api(app):
    api = Api(
        plugins=[
            create_api_spec_plugin(app),
        ],
        app=app,
    )
    api.route(TagList, 'tag_list', '/api/tags/', tag='Tag')
    api.route(TagDetail, 'tag_detail', '/api/tags/<int:id>/', tag='Tag')

    api.route(UserList, 'user_list', '/api/users/', tag='User')
    api.route(UserDetail, 'user_detail', '/api/users/<int:id>/', tag='User')

    api.route(AuthorList, 'author_list', '/api/authors/', tag='Author')
    api.route(AuthorDetail, 'author_detail', '/api/authors/<int:id>/',
              tag='Author')

    api.route(ArticleList, 'article_list', '/api/articles/', tag='Article')
    api.route(ArticleDetail, 'article_detail', '/api/articles/<int:id>/',
              tag='Article')


def register_blueprints(app: Flask):
    from blog.user.views import user
    from blog.auth.views import auth
    from blog.article.views import article
    from blog.author.views import author
    from blog import admin

    app.register_blueprint(user)
    app.register_blueprint(article)
    app.register_blueprint(auth)
    app.register_blueprint(author)

    admin.register_views()


def register_commands(app):
    app.cli.add_command(commands.init_db)
    app.cli.add_command(commands.create_users)
    app.cli.add_command(commands.create_tags)
