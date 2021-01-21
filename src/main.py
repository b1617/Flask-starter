import os
from flask import Flask
from .views.user import user
from .extensions.database import db
from .extensions.marshmallow import ma
from .extensions.migrate import mi

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
        os.path.join(basedir, 'users.sqlite')
    db.init_app(app)
    ma.init_app(app)
    mi.init_app(app, db)
    app.register_blueprint(user)
    return app
