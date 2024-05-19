from flask import jsonify, Blueprint, request
from app.models import db, User, Workout, Exercise, Repetition
from app.mapping import UserSchema, WorkoutSchema, ExerciseSchema, RepetitionSchema

exercise_bp = Blueprint('exercise', __name__)
#exercise_service = ExerciseService()
exercise_schema = ExerciseSchema()


@exercise_bp.route('/', methods=['GET'])
def get_all_exercises():
    exercises = Exercise.query.all()
    resp = exercise_schema.dump(exercises, many=True)
    return jsonify(resp), 200

@exercise_bp.route('/<int:id>', methods=['GET'])
def get_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    resp = exercise_schema.dump(exercise)
    return jsonify(resp), 200

@exercise_bp.route('/', methods=['POST'])
def create_exercise():
    exercise_data = request.json
    exercise = Exercise(name=exercise_data['name'], description=exercise_data['description'])
    db.session.add(exercise)
    db.session.commit()
    resp = exercise_schema.dump(exercise)
    return jsonify(resp), 201

@exercise_bp.route('/<int:id>', methods=['PUT'])
def update_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    exercise_data = request.json
    exercise.name = exercise_data['name']
    exercise.description = exercise_data['description']
    db.session.commit()
    resp = exercise_schema.dump(exercise)
    return jsonify(resp), 200

@exercise_bp.route('/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    db.session.delete(exercise)
    db.session.commit()
    return jsonify("Ejercicio eliminado correctamente"), 204
