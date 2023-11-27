from flask import Flask
from config import Config
from flask_login import LoginManager, UserMixin
from app.models import db, User
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

login_manager.init_app(app)

db.init_app(app)
migrate = Migrate(app, db)


login_manager.login_view = 'auth.login'
login_manager.login_message = "Only registered Pokémon Trainers can access this area! Please log in to unleash the power of your Poké-Clash journey!🔐"
login_manager.login_message_category = 'danger'


from app.blueprints.auth import auth
from app.blueprints.main import main
from app.blueprints.teams import teams
app.register_blueprint(auth)
app.register_blueprint(main)
app.register_blueprint(teams)


