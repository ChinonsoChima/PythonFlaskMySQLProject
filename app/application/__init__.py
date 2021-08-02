from flask import Flask
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

mysql = MySQL(cursorclass=DictCursor)

def init_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    mysql.init_app(app)

    with app.app_context():

        from . import routes

    return app