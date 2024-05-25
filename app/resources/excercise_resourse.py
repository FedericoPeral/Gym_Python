from flask import jsonify, Blueprint, request
from app.models import db, User, Workout, Excercise, Repetition
from app.mapping import UserSchema, WorkoutSchema, ExcerciseSchema, RepetitionSchema
from app.services import ExcerciseService
excercise_bp = Blueprint('excercise', __name__)
excercise_service = ExcerciseService()
excercise_schema = ExcerciseSchema()


@excercise_bp.route('/', methods=['GET'])
def get_all_excercises():
    excercises = Excercise.query.all()
    resp = excercise_schema.dump(excercises, many=True)
    return jsonify(resp), 200

@excercise_bp.route('/<int:id>', methods=['GET'])
def get_excercise(id):
    excercise = Excercise.query.get_or_404(id)
    resp = excercise_schema.dump(excercise)
    return jsonify(resp), 200

@excercise_bp.route('/', methods=['POST'])
def create_excercise():
    excercise_data = request.json
    excercise = Excercise(name=excercise_data['name'], description=excercise_data['description'])
    db.session.add(excercise)
    db.session.commit()
    resp = excercise_schema.dump(excercise)
    return jsonify(resp), 201

@excercise_bp.route('/<int:id>', methods=['PUT'])
def update_excercise(id):
    excercise = Excercise.query.get_or_404(id)
    excercise_data = request.json
    excercise.name = excercise_data['name']
    excercise.description = excercise_data['description']
    db.session.commit()
    resp = excercise_schema.dump(excercise)
    return jsonify(resp), 200

@excercise_bp.route('/<int:id>', methods=['DELETE'])
def delete_excercise(id):
    excercise = Excercise.query.get_or_404(id)
    db.session.delete(excercise)
    db.session.commit()
    return jsonify("Ejercicio eliminado correctamente"), 204
