# book_proj_mod/catalog/__init__.py

from flask import Blueprint

main = Blueprint('main', __name__, template_folder='templates')

from book_proj_mod.catalog import routes, models