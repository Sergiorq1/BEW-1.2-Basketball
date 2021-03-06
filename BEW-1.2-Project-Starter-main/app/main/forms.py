# Create your forms here.
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SelectField, SubmitField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import Player, Team, Match, Skill

class TeamForm(FlaskForm):
    "Form to create team"
    team_name = StringField("Team Name",
        validators=[DataRequired(), Length(min=3, max=80)])
    add_member = QuerySelectField("Add Member",
        query_factory=lambda: Player.query, allow_blank=False)
    skill = SelectField('Skill', choices=Skill.choices())

# class MatchTeam(FlaskForm):
#     "Form to create A match"
#     team

    
    


