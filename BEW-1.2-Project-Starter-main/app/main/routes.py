from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date, datetime
from app.models import Player, Skill, Team, Match
from app.main.forms import TeamForm
from app import bcrypt
from app import app, db
main = Blueprint('main', __name__)

@main.route('/')
def homepage():
    all_teams = Team.query.all()
    all_players = Player.query.all()
    return render_template('home.html',
        all_teams=all_teams, all_players=all_players)

# Create your routes here.
@main.route('/create_team', methods=['GET', 'POST'])
@login_required
def create_team():
    form = TeamForm()

    if form.validate_on_submit(): 
        new_team = Team(
            name=form.name.data,
            player=form.player.data,
        )
        db.session.add(new_team)
        db.session.commit()

        flash('New Team was created successfully!')
        return redirect(url_for('main.team_detail', team_id=new_team.id))
    return render_template('create_team.html', form=form)


@main.route('/team/<team_id>', methods=['GET', 'POST'])
def team_detail(team_id):
    team = Team.query.get(team_id)
    form = TeamForm(obj=team)
    
    # if form was submitted and contained no errors
    if form.validate_on_submit():
        team.name = form.name.data
        team.player = form.player.data
        
        db.session.add(team)
        db.session.commit()

        flash('Team was updated successfully!')
        return redirect(url_for('main.team_detail', team_id=team_id))

    return render_template('team_detail.html', team=team, form=form)


@main.route('/profile/<username>')
def profile(username):
    user = Player.query.filter_by(username=username).one()
    return render_template('profile.html', user=user)