"""
The flask application package.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from WhatsUp.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from WhatsUp.accounts.routes import accounts
    from WhatsUp.contacts.routes import contacts
    from WhatsUp.main.routes import main
    from WhatsUp.chats.routes import chats
    from WhatsUp.errors.handelers import errors
    app.register_blueprint(accounts)
    app.register_blueprint(contacts)
    app.register_blueprint(main)
    app.register_blueprint(chats)
    app.register_blueprint(errors)

    return app

