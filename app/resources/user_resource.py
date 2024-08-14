from flask import jsonify, Blueprint, request
from app.mapping import UserSchema
from app.services import UserService

user = Blueprint('user', __name__)
service = UserService()
user_schema = UserSchema()

"""
Obtiene todos las users
"""
@user.route('/user', methods=['GET'])
def all():
    resp = user_schema.dump(service.get_all(), many=True) 
    return resp, 200

"""
filtra los users por su inicial
"""
@user.route('/users_inicial/<string:inicial>', methods=['GET'])
def all_inv(inicial):
    resp = user_schema.dump(service.get_all_inicial(inicial), many=True) 
    return resp, 200

"""
Obtiene una user por id
"""
@user.route('/users/<int:id>', methods=['GET'])
def one(id):
    resp = user_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Crea un nuevo user
"""
@user.route('/users', methods=['POST'])
def create():
    usuario = user_schema.load(request.json)
    resp = user_schema.dump(service.create(usuario))
    return resp, 201

"""
Actualiza un user existente
"""
@user.route('/users/<int:id>', methods=['PUT'])
def update(id):
    usuario = user_schema.load(request.json)
    resp = user_schema.dump(service.update(id, usuario))
    return resp, 200

"""
Elimina un user existente
"""
@user.route('/users/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "user eliminado correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar el user"
    return jsonify(msg), 204