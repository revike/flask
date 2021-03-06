from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload

from blog.extensions import db
from blog.forms.article import CreateArticleForm
from blog.models_db.models import Tag, Article, Author, User


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
    form.tags.choices = [(tag.id, tag.name) for tag in
                         Tag.query.order_by('name')]

    if request.method == 'POST':

        if form.validate_on_submit():
            article_ = Article(title=form.title.data.strip(),
                               text=form.text.data)

            author = Author(user_id=current_user.id)
            article_.author_id = current_user.id

            if form.tags.data:
                selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
                for tag in selected_tags:
                    article_.tags.append(tag)

            author_db = Author.query.filter_by(user_id=current_user.id).first()
            if not author_db:
                db.session.add(author)

            db.session.flush()
            db.session.add(article_)
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
    _article: Article = Article.query.filter_by(id=pk).options(
        joinedload(Article.tags)).one_or_none()
    if not _article:
        return redirect('/articles/')

    author = User.query.filter_by(id=_article.author_id).one_or_none()
    return render_template(
        'articles/details.html',
        title_body=_article.title,
        article=_article.id,
        text=_article.text,
        author=author.username,
        _article=_article,
        title=f'article - {_article.title}',
    )
