from flask import jsonify, Blueprint, request
from app.mapping import DetallesNacimientoSchema
from app.services.detalles_nacimiento_services import DetallesNacimientoService

detalles_nacimiento = Blueprint('detalles_nacimiento', __name__)
service = DetallesNacimientoService()
detalles_nacimiento_schema = DetallesNacimientoSchema()

"""
Obtiene todos los detalles_nacimientos
"""
@detalles_nacimiento.route('/detalles_nacimiento', methods=['GET'])
def all():
    resp = detalles_nacimiento_schema.dump(service.get_all(), many=True) 
    return resp, 200

"""
Obtiene una detalles_nacimientos por id
"""
@detalles_nacimiento.route('/detalles_nacimientos/<int:id>', methods=['GET'])
def one(id):
    resp = detalles_nacimiento_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Elimina un detalles_nacimiento existente
"""
@detalles_nacimiento.route('/detalles_nacimientos/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "detalles_nacimiento eliminado correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar el detalles_nacimiento"
    return jsonify(msg), 204