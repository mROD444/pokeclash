from app.blueprints.main import main
from flask import render_template, request
from flask_login import login_required
import requests



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