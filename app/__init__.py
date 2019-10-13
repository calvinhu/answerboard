from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_user import UserManager
from config import Config

db = SQLAlchemy()

def create_app():

	app = Flask(__name__)
	db.init_app(app)
	app.config.from_object(Config)

	with app.app_context():
		from . import routes, models

		migrate = Migrate(app, db)
		login = LoginManager(app)
		login.login_view = 'login'
		user_manager = UserManager(app, db, models.User)

		db.create_all()

		return app