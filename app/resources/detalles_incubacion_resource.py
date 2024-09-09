from flask import jsonify, Blueprint, request
from app.mapping.detalles_incubacion_schema import DetallesIncubacionSchema
from app.services.detalles_incubacion_services import DetallesIncubacionService

detalles_incubacion = Blueprint('detalles_incubacion', __name__)
service = DetallesIncubacionService()
detalles_incubacion_schema = DetallesIncubacionSchema()

"""
Obtiene todos los detalles_incubaciones
"""
@detalles_incubacion.route('/detalles_incubacion', methods=['GET'])
def all():
    resp = detalles_incubacion_schema.dump(service.get_all(), many=True) 
    return resp, 200

"""
Obtiene una detalles_incubaciones por id
"""
@detalles_incubacion.route('/detalles_incubaciones/<int:id>', methods=['GET'])
def one(id):
    resp = detalles_incubacion_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Elimina un detalles_incubacion existente
"""
@detalles_incubacion.route('/detalles_incubaciones/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "detalles_incubacion eliminado correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar el detalles_incubacion"
    return jsonify(msg), 204