from . import auth
from .forms import LoginForm, SignUpForm
from flask import request, flash, redirect, url_for, render_template
from app.models import User, db
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user, login_required

#login
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        queried_user = User.query.filter(User.email == email).first()
        if queried_user and check_password_hash(queried_user.password, password):
            login_user(queried_user)
            flash(f"Hello, {queried_user.username}! You've successfully logged into Poké-Clash!🎉", 'info')
            return redirect(url_for('main.home'))
        else:
            return "Sorry, Trainer! Seems like the email or password is not quite right... Double-check and try again!"
    else:
        return render_template('login.html', form=form)



#signup
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        user = User(username, email, password)

        db.session.add(user)
        db.session.commit()

        flash(f"Congratulations, {username}! You've successfully joined our Poké-Clash community!🎉 Your journey to become a Pokémon master is just beginning!", "success")
        return redirect(url_for('auth.login'))
    else:
        return render_template('signup.html', form=form)




#logout
@auth.route('/logout')
@login_required
def logout():
    flash('Until your next adventure, Trainer! ⚡', 'info')
    logout_user()
    return redirect(url_for('auth.login'))