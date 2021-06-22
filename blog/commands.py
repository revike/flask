import click
from werkzeug.security import generate_password_hash

from blog.extensions import db
from blog.models.article import Article
from blog.models.user import User


@click.command('init-db')
def init_db():
    from wsgi import app
    with app.app_context():
        db.create_all()
        print('init_db! done!')


@click.command('create-users')
def create_users():
    from wsgi import app
    with app.app_context():
        admin = User(
            username='admin',
            email='admin@mail.ru',
            password=generate_password_hash('123'),
            is_staff=True
        )

        james = User(
            username='james',
            email='james@mail.ru',
            password=generate_password_hash('12345')
        )

        db.session.add(admin)
        db.session.add(james)

        db.session.commit()
        print('create users!')


@click.command('create-articles')
def create_articles():
    from wsgi import app
    with app.app_context():
        article_1 = Article(
            title='some title #1',
            text='some text #1',
            author_id=1
        )

        article_2 = Article(
            title='some title #2',
            text='some text #2',
            author_id=2
        )

        db.session.add(article_1)
        db.session.add(article_2)

        db.session.commit()

        print('create articles!')
