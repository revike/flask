import click
from werkzeug.security import generate_password_hash

from blog.extensions import db
from blog.models_db.models import User, Tag


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


@click.command('create-tags')
def create_tags():
    from wsgi import app
    with app.app_context():
        tags = ('flask', 'django', 'python', 'gb')
        for tag in tags:
            db.session.add(Tag(name=tag))
        db.session.commit()

    print('create tags!')
