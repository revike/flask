from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from blog.extensions import db
from blog.forms.user import UserRegisterForm, UserLoginForm
from blog.models.user import User

auth = Blueprint('auth', __name__, static_folder='../static')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.get_user', pk=current_user.id))

    form = UserLoginForm(request.form)

    if request.method == 'POST':
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash('Неверный логин или пароль')
            return redirect(url_for('.login'))

        login_user(user)
        return redirect(url_for('user.get_user', pk=user.id))

    return render_template(
        'auth/login.html',
        form=form,
        tittle_body='login',
        title='login',
    )


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('user.get_user', pk=current_user.id))

    form = UserRegisterForm(request.form)
    errors = []
    if request.method == 'POST' and form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append('email not uniq')
            return render_template('auth/register.html', form=form)

        user_ = User(
            username=form.username.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data)
        )

        db.session.add(user_)
        db.session.commit()

        login_user(user_)

    return render_template(
        'auth/register.html',
        form=form,
        errors = errors,
        tittle_body='register',
        title='register',
    )
