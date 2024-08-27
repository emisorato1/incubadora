from flask import jsonify, Blueprint, request
from app.mapping import NacimientoSchema
from app.services.nacimiento_services import NacimientoService

nacimiento = Blueprint('nacimiento', __name__)
service = NacimientoService()
nacimiento_schema = NacimientoSchema()

"""
Obtiene todos los nacimientos
"""
@nacimiento.route('/nacimiento', methods=['GET'])
def all():
    resp = nacimiento_schema.dump(service.get_all(), many=True) 
    return resp, 200

"""
Obtiene una nacimientos por id
"""
@nacimiento.route('/nacimientos/<int:id>', methods=['GET'])
def one(id):
    resp = nacimiento_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Crea nuevo nacimiento
"""
@nacimiento.route('/nacimientos', methods=['POST'])
def create():
    usuario = nacimiento_schema.load(request.json)
    resp = nacimiento_schema.dump(service.create(usuario))
    return resp, 201

"""
Elimina un nacimiento existente
"""
@nacimiento.route('/nacimientos/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "nacimiento eliminado correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar el nacimiento"
    return jsonify(msg), 204