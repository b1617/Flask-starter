import json
from flask import Blueprint, jsonify, request

config = {
    'name' : 'user',
    'route' : '/api/users'
}

blueprint = Blueprint(config.get('name'), __name__)

@blueprint.route('{}'.format(config.get('route')), methods=['GET'])
def get():
    return jsonify({'get' : 'get'})


@blueprint.route('{}'.format(config.get('route')), methods=['POST'])
def post(**kwargs):
    data = json.loads(request.data) if request.data else None
    print('data', data)
    return jsonify({'add' : 'add'})