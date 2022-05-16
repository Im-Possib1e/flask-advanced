# book_proj)mod/auth/__init__.py

from flask import Blueprint

authentication = Blueprint('authentication', __name__, template_folder='templates')

from book_proj_mod.auth import routes, models
