from werkzeug.security import generate_password_hash

from blog.app import create_app
from blog.models.article import Article
from blog.models.user import User
from blog.models.database import db

app = create_app()


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('init_db! done!')


@app.cli.command('create-users')
def create_users():
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


@app.cli.command('create-articles')
def create_articles():
    article_1 = Article(
        title='some title #1',
        text='some text #1',
        author=1
    )

    article_2 = Article(
        title='some title #2',
        text='some text #2',
        author=2
    )

    db.session.add(article_1)
    db.session.add(article_2)

    db.session.commit()

    print('create articles!')
