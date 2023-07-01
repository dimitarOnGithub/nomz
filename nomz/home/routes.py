import json
from datetime import datetime
import ast
from flask import Blueprint, request, render_template, flash, url_for
from flask_login import current_user
from werkzeug.utils import redirect
import os
import logging

from nomz.home.models.category import Category

home = Blueprint('home', __name__, template_folder='templates')


@home.route("/")
def home_page():
    categories = Category.query.all()
    return render_template('home.html', categories=categories)
