from flask import render_template, redirect, Blueprint
from flask_login import login_required

from blog.models.user import Author

author = Blueprint('author', __name__,
                   static_folder='../static', url_prefix='/authors')


@author.route('/')
def author_list():
    authors = Author.query.all()
    return render_template(
        'authors/list.html',
        authors=authors,
        title_body='authors:',
        title='author list'
    )


@author.route('/<int:pk>')
@login_required
def get_author(pk: int):
    author_ = Author.query.filter_by(user_id=pk).one_or_none()
    if not author_:
        return redirect('/authors/')
    return render_template(
        'authors/details.html',
        author=author_,
        title_body='author:',
        title=f'author - {author_.user.username}',
    )
