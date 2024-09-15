from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user
# from .models import User
from . import auth_bp

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method == 'POST':
    #     username = request.form['username']
    #     password = request.form['password']
    #     user = User.query.filter_by(username=username).first()
    #     if user and user.check_password(password):
    #         login_user(user)
    #         return redirect(url_for('admin.dashboard'))
    #     else:
    #         flash('Invalid username or password')
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
