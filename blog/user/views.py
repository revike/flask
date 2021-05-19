from flask import Blueprint, render_template, redirect
from flask_login import login_required

from blog.models.user import User

user = Blueprint('user', __name__,
                 static_folder='../static', url_prefix='/users')


@user.route('/')
def user_list():
    users = User.query.all()
    return render_template(
        'users/list.html',
        users=users,
        title_body='users:',
        title='user list'
    )


@user.route('/<int:pk>')
@login_required
def get_user(pk: int):
    user_ = User.query.filter_by(id=pk).one_or_none()
    if not user_:
        return redirect('/users/')
    return render_template(
        'users/details.html',
        user=user_,
        title_body='user:',
        title=f'user - {user_.username}',
    )
