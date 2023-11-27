from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin, LoginManager
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique = True)
    email = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)


class PokemonTeam(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    pokemon1 = db.Column(db.String, nullable=True, unique = True)
    pokemon2 = db.Column(db.String, nullable=True, unique = True)
    pokemon3 = db.Column(db.String, nullable=True, unique = True)
    pokemon4 = db.Column(db.String, nullable=True, unique = True)
    pokemon5 = db.Column(db.String, nullable=True, unique = True)

    def __init__(self, pokemon1, pokemon2, pokemon3, pokemon4, pokemon5):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.pokemon3 = pokemon3
        self.pokemon4 = pokemon4
        self.pokemon5 = pokemon5