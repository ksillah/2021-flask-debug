from flask import Blueprint, render_template, flash, redirect, url_for, request
from may_blog.forms import UserLoginForm, UserInfoForm
from may_blog.models import User, check_password_hash

from flask_login import login_user, logout_user, current_user, login_required


auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserInfoForm()

    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        print("\n",username, password, email)
        
        user = User(username, email, password)
        db.session.add(user)
        db.session.commit()

        flash(f'You have successfully created a user account {email}', 'user-created')
        return redirect(url_for('site.home'))

    return render_template('signup.html', form = form)


@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = UserLoginForm()
    if request.method =='POST' and form.validate_on_submit():
        email = form.email
        password = form.password.data
        print(email, password)
        
        logged_user = User.query.filter(User.email == email).first()

        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            flash('You were successfully logged in: Via Email/Password', 'auth-success')
            return redirect(url_for('site.home'))
        else:
            flash('Your Email/Password is incorrect', 'auth-failed')
            return redirect(url_for('auth.signin'))

    return render_template('signin.html', form = form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('site.home'))
