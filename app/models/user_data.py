from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class UserData(db.Model):
    __tablename__ = 'users_data'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    surname: str = db.Column(db.String(80), nullable=False)
    phone: str = db.Column(db.String(120), nullable=False)
    address: str = db.Column(db.String(120), nullable=False)
    city: str   = db.Column(db.String(120), nullable=False)
    country: str = db.Column(db.String(120), nullable=False)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
    #user = db.relationship("User", back_populates='data', uselist=False)

#from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     # Otros campos según tus necesidades

# class Workout(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     date_time = db.Column(db.DateTime, nullable=False)
#     # Otros campos según tus necesidades

# class Exercise(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.Text, nullable=False)
#     # Otros campos según tus necesidades

# class WorkoutDetail(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'), nullable=False)
#     exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'), nullable=False)

# class Repetition(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     workout_detail_id = db.Column(db.Integer, db.ForeignKey('workout_detail.id'), nullable=False)
#     series_number = db.Column(db.Integer, nullable=False)
#     num_repetitions = db.Column(db.Integer, nullable=False)
