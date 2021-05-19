from flask import Blueprint, render_template, redirect
from flask_login import login_required

from blog.models.article import Article
from blog.models.user import User

article = Blueprint('article', __name__,
                    url_prefix='/articles', static_folder='../static')


@article.route('/')
@login_required
def article_list():
    articles = Article.query.all()
    return render_template(
        'articles/list.html',
        articles=articles,
        title_body='articles:',
        title='article list'
    )


@article.route('/<int:pk>')
@login_required
def get_article(pk: int):
    articles = Article.query.filter_by(id=pk).one_or_none()
    if not articles:
        return redirect('/articles/')
    
    author = User.query.filter_by(id=articles.author).one_or_none()
    return render_template(
        'articles/details.html',
        title_body=articles.title,
        article=articles.id,
        text=articles.text,
        author=author.username,
        title=f'article - {articles.title}'
    )
