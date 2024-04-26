from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Exercise(db.Model):
    __tablename__ = 'exercises'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(100), nullable=False)
    description: str = db.Column(db.Text, nullable=False)
    workout_id: int = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable=False)
