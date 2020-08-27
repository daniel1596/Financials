from flask import render_template

from . import Blueprint

pages = Blueprint("pages", __name__)


@pages.route('/')
def hello_world():
    return render_template('index.html')