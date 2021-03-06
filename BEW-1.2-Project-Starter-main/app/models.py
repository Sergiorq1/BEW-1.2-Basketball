# Have matchup set up
from app import db
from flask_login import UserMixin
from sqlalchemy.orm import backref
import enum

class FormEnum(enum.Enum):
    """Helper class to make it easier to use enums with forms."""
    @classmethod
    def choices(cls):
        return [(choice.name, choice) for choice in cls]

    def __str__(self):
        return str(self.value)

class Skill(FormEnum):
    BEGINNER = 'Beginner'
    INTERMEDIATE = 'Intermediate'
    PRO = 'Pro'
    STAR = 'Star'

class Player(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    team = db.relationship('Team', secondary='player_team', back_populates="player")
    skill = db.Column(db.Enum(Skill), default=Skill.INTERMEDIATE)

    def __repr__(self):
        return f'<player: {self.username}'


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    player = db.relationship('Player', secondary='player_team', back_populates='team')

    def __str__(self):
        return f'<Team: {self.name}>'

    def __repr__(self):
        return f'<Team: {self.name}>'

player_team_table = db.Table('player_team',
    db.Column('team_id', db.Integer, db.ForeignKey('team.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('player.id'))
)

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

