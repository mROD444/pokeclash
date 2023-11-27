from . import teams
from flask import request, flash, redirect, url_for, render_template
from app.models import Team, db
from .forms import TeamForm
from flask_login import current_user, login_required

#choosing a pokemon
@teams.route('/choose_pokemon', methods=['GET', 'POST'])
@login_required
def choose_pokemon():
    form = TeamForm()
    if request.method == 'POST' and form.validate_on_submit():
        pokemon1 = form.pokemon1.data
        pokemon2 = form.pokemon2.data
        pokemon3 = form.pokemon3.data
        pokemon4 = form.pokemon4.data
        pokemon5 = form.pokemon5.data
        user_id = current_user.id

        team = Team(pokemon1,pokemon2,pokemon3,pokemon4,pokemon5, user_id)

        db.session.add(team)
        db.session.commit()

        flash(f"Congratulations, {{current_user.id}}! You've successfully added a new Pokémon to your team. Get ready to conquer the Pokémon world with your strengthened lineup!", "success")
        return redirect(url_for('teams.updated_roster'))
    else:
        return redirect(render_template('choose_pokemon.html', form=form))
    


@teams.route('/roster')
@login_required
def roster():
    full_roster = Team.query.all()
    return render_template('roster.html', full_roster=full_roster)