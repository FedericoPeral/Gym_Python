from flask import jsonify, Blueprint, request
from app.models import db, User

user_bp = Blueprint('user', __name__)
user_service = UserService()
user_schema = UserSchema()


@user_bp.route('/', methods=['GET'])
def get_all_users():
    users = User.query.all()
    resp = user_schema.dump(users, many=True)
    return jsonify(resp), 200

@user_bp.route('/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    resp = user_schema.dump(user)
    return jsonify(resp), 200

@user_bp.route('/', methods=['POST'])
def create_user():
    user_data = request.json
    user = User(username=user_data['username'], password=user_data['password'], email=user_data['email'])
    db.session.add(user)
    db.session.commit()
    resp = user_schema.dump(user)
    return jsonify(resp), 201

@user_bp.route('/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    user_data = request.json
    user.username = user_data['username']
    user.password = user_data['password']
    user.email = user_data['email']
    db.session.commit()
    resp = user_schema.dump(user)
    return jsonify(resp), 200

@user_bp.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify("Usuario eliminado correctamente"), 204