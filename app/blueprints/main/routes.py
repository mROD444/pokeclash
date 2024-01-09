from app.blueprints.main import main
from flask import render_template, request
from flask_login import login_required, current_user
import requests
from app import db
from app.models import Pokemon
from . import main
from flask import flash, redirect, url_for


#home
@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')

#search
@main.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    if request.method == 'POST':
        pokemon = request.form.get('pokeName') 
        poke_data = get_pokemon_data(pokemon)
        return render_template('search.html', poke_data=poke_data)
    else:
        return render_template('search.html')

    

#SEARCH
def get_pokemon_data(number):
    url = f'https://pokeapi.co/api/v2/pokemon/{number}'
    response = requests.get(url)
    data = response.json()

    pokemon = {
        'name': data['forms'][0]['name'],
        'ability': data['abilities'][0]['ability']['name'],
        'base_experience': data['base_experience'],
        'image': data['sprites']['front_default']
    }

    return pokemon


#ROSTER

@main.route('/roster', methods=['GET', 'POST'])
@login_required
def roster():
    if request.method == 'POST':
        pokemon_name = request.form.get('pokeName')
        if not Pokemon.query.filter_by(name=pokemon_name, user_id=current_user.id).first():
            new_pokemon = Pokemon(name=pokemon_name, user_id=current_user.id)
            db.session.add(new_pokemon)
            db.session.commit()
            flash(f'{pokemon_name} added to your roster!', 'success')
        else:
            flash(f'{pokemon_name} is already in your roster!', 'info')
        return redirect(url_for('main.roster'))
    user_roster = Pokemon.query.filter_by(user_id=current_user.id).all()
    return render_template('roster.html', user_roster=user_roster)

#releasing pokemon


@main.route('/release/<int:pokemon_id>', methods=['GET'])
@login_required
def remove_pokemon(pokemon_id):
    pokemon_to_release = Pokemon.query.get(pokemon_id)
    if pokemon_to_release:
        db.session.delete(pokemon_to_release)
        db.session.commit()
        flash(f'{pokemon_to_release.name} removed from your roster!', 'success')
    else:
        flash('Pokemon not found in your roster!', 'danger')
    return redirect(url_for('main.roster'))



#view team
@main.route('/team')
@login_required
def team():
    my_team = current_user.Pokemon
    return render_template('team.html', my_team=my_team)



