from flask import jsonify, Blueprint, request
from app.mapping import IncubacionSchema
from app.services.incubacion_services import IncubacionService

incubacion = Blueprint('incubacion', __name__)
service = IncubacionService()
incubacion_schema = IncubacionSchema()

"""
Obtiene todas las incubaciones
"""
@incubacion.route('/incubacion', methods=['GET'])
def all():
    resp = incubacion_schema.dump(service.get_all(), many=True) 
    return resp, 200

"""
Obtiene una incubaciones por id
"""
@incubacion.route('/incubaciones/<int:id>', methods=['GET'])
def one(id):
    resp = incubacion_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Crea nueva incubacion
"""
@incubacion.route('/incubaciones', methods=['POST'])
def create():
    usuario = incubacion_schema.load(request.json)
    resp = incubacion_schema.dump(service.create(usuario))
    return resp, 201

"""
Elimina una incubacion existente
"""
@incubacion.route('/incubaciones/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "incubacion eliminada correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar el incubacion"
    return jsonify(msg), 204