from flask import jsonify, Blueprint, request
from app.models import db, User, Workout, Excercise, Repetition
from app.mapping import UserSchema, WorkoutSchema, ExcerciseSchema, RepetitionSchema
from app.services import RepetitionService
repetition_bp = Blueprint('repetition', __name__)
repetition_service = RepetitionService()
repetition_schema = RepetitionSchema()

@repetition_bp.route('/', methods=['GET'])
def get_all_repetitions():
    repetitions = Repetition.query.all()
    resp = repetition_schema.dump(repetitions, many=True)
    return jsonify(resp), 200

@repetition_bp.route('/<int:id>', methods=['GET'])
def get_repetition(id):
    repetition = Repetition.query.get_or_404(id)
    resp = repetition_schema.dump(repetition)
    return jsonify(resp), 200

@repetition_bp.route('/', methods=['POST'])
def create_repetition():
    repetition_data = request.json
    repetition = Repetition(workout_id=repetition_data['workout_id'], excercise_id=repetition_data['excercise_id'], series_number=repetition_data['series_number'], num_repetitions=repetition_data['num_repetitions'], peso=repetition_data['peso'])
    db.session.add(repetition)
    db.session.commit()
    resp = repetition_schema.dump(repetition)
    return jsonify(resp), 201

@repetition_bp.route('/<int:id>', methods=['PUT'])
def update_repetition(id):
    repetition = Repetition.query.get_or_404(id)
    repetition_data = request.json
    repetition.workout_id = repetition_data['workout_id']
    repetition.excercise_id = repetition_data['excercise_id']
    repetition.series_number = repetition_data['series_number']
    repetition.num_repetitions = repetition_data['num_repetitions']
    repetition.peso = repetition_data['peso']
    db.session.commit()
    resp = repetition_schema.dump(repetition)
    return jsonify(resp), 200

@repetition_bp.route('/<int:id>', methods=['DELETE'])
def delete_repetition(id):
    repetition = Repetition.query.get_or_404(id)
    db.session.delete(repetition)
    db.session.commit()
    return jsonify("Repetición eliminada correctamente"), 204