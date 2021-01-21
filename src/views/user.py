from flask import Blueprint, request, jsonify
from src.models.user import User, user_schema, users_schema
from src.extensions.database import db

config = {
    'name': 'user',
    'route': '/users'
}


user = Blueprint(config.get('name'), __name__)


@user.route('{}'.format(config.get('route')), methods=['POST'])
def create_user():
    request_data = request.json
    first_name = request_data["last_name"]
    last_name = request_data["last_name"]
    email = request_data["email"]
    new_user = User(first_name=first_name, last_name=last_name,
                email=email)
                
    db.session.add(new_user)
    db.session.commit()

    return jsonify(user_schema.dump(new_user))


@user.route('{}'.format(config.get('route')), methods=["GET"])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)

    return jsonify(result)


@user.route('{}/<id>'.format(config.get('route')), methods=["GET"])
def get_user_by_id(id):
    user = User.query.get(id)
    result = user_schema.dump(user)

    return jsonify(result)


@user.route('{}/<id>'.format(config.get('route')), methods=['PUT'])
def update_user(id):
    request_data = request.json
    user = User.query.get(id)
    user.first_name = request_data["first_name"]
    user.last_name = request_data["last_name"]
    user.email = request_data["email"]

    db.session.add(user)
    db.session.commit()

    return jsonify(user_schema.dump(user))


@user.route('{}/<id>'.format(config.get('route')), methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)

    db.session.delete(user)
    db.session.commit()

    return jsonify(user_schema.dump(user))
