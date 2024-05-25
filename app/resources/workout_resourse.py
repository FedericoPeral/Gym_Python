from flask import jsonify, Blueprint, request
from app.models import db, User, Workout, Excercise, Repetition
from app.mapping import UserSchema, WorkoutSchema, ExcerciseSchema, RepetitionSchema
from app.services import WorkoutService
workout_bp = Blueprint('workout', __name__)
workout_service = WorkoutService()
workout_schema = WorkoutSchema()

@workout_bp.route('/', methods=['GET'])
def get_all_workouts():
    workouts = Workout.query.all()
    resp = workout_schema.dump(workouts, many=True)
    return jsonify(resp), 200

@workout_bp.route('/<int:id>', methods=['GET'])
def get_workout(id):
    workout = Workout.query.get_or_404(id)
    resp = workout_schema.dump(workout)
    return jsonify(resp), 200

@workout_bp.route('/', methods=['POST'])
def create_workout():
    workout_data = request.json
    workout = Workout(date_time=workout_data['date_time'], user_id=workout_data['user_id'])
    db.session.add(workout)
    db.session.commit()
    resp = workout_schema.dump(workout)
    return jsonify(resp), 201

@workout_bp.route('/<int:id>', methods=['PUT'])
def update_workout(id):
    workout = Workout.query.get_or_404(id)
    workout_data = request.json
    workout.date_time = workout_data['date_time']
    workout.user_id = workout_data['user_id']
    db.session.commit()
    resp = workout_schema.dump(workout)
    return jsonify(resp), 200

@workout_bp.route('/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = Workout.query.get_or_404(id)
    db.session.delete(workout)
    db.session.commit()
    return jsonify("Entrenamiento eliminado correctamente"), 204

