from flask import Blueprint

teams = Blueprint('teams', __name__, template_folder='teams_templates')

from app.blueprints.teams import teams