from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user

from blog.extensions import db
from blog.forms.article import CreateArticleForm
from blog.models.article import Article
from blog.models.user import User, Author

article = Blueprint('article', __name__,
                    url_prefix='', static_folder='../static')


@article.route('/', methods=['GET'])
@login_required
def article_list():
    articles = Article.query.all()
    return render_template(
        'articles/list.html',
        articles=articles,
        title_body='articles:',
        title='article list'
    )


@article.route('/create', methods=['GET', 'POST'])
@login_required
def create_article():
    form = CreateArticleForm(request.form)
    if request.method == 'POST':

        if form.validate_on_submit():
            article_ = Article(title=form.title.data.strip(), text=form.text.data)

            author = Author(user_id=current_user.id)
            article_.author_id = current_user.id

            db.session.add(article_)

            author_db = Author.query.filter_by(id=current_user.id)
            if not author_db:
                db.session.add(author)

            db.session.commit()
            return redirect(url_for('article.get_article', pk=article_.id))

    return render_template(
        'articles/create.html',
        form=form,
        title_body='create article',
        title='create article'
    )


@article.route('/<int:pk>')
@login_required
def get_article(pk: int):
    articles = Article.query.filter_by(id=pk).one_or_none()
    if not articles:
        return redirect('/articles/')

    author = User.query.filter_by(id=articles.author_id).one_or_none()
    return render_template(
        'articles/details.html',
        title_body=articles.title,
        article=articles.id,
        text=articles.text,
        author=author.username,
        title=f'article - {articles.title}'
    )
