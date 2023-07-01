import json
from datetime import datetime
import ast
from flask import Blueprint, request, render_template, flash, url_for
from flask_login import current_user, login_user
from werkzeug.utils import redirect
import os
import logging

from nomz import bcrypt
from nomz.auth.models.user import User
from nomz.auth.forms.login import LoginForm

auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route("/login", methods=["GET", "POST"])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('home.home_page'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            flash(f"Welcome on board, {user.username}")
            login_user(user)
            return redirect(url_for('home.home_page'))
        else:
            flash("Nope")
    return render_template("login.html", form=login_form)

