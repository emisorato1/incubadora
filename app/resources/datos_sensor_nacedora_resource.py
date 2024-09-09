from flask import jsonify, Blueprint, request
from app.mapping import DatosSensorNacedoraSchema
from app.services.datos_sensor_nacedora_services import DatosSensorNacedoraService

datos_sensores_nacedora = Blueprint('datos_sensores_nacedora', __name__)
service = DatosSensorNacedoraService()
datos_sensores_nacedora_schema = DatosSensorNacedoraSchema()

"""
Obtiene todos los datos_sensores_nacedoras
"""
@datos_sensores_nacedora.route('/datos_sensores_nacedora', methods=['GET'])
def all():
    resp = datos_sensores_nacedora_schema.dump(service.get_all(), many=True) 
    return resp, 200

"""
Obtiene una datos_sensores_nacedoras por id
"""
@datos_sensores_nacedora.route('/datos_sensores_nacedoras/<int:id>', methods=['GET'])
def one(id):
    resp = datos_sensores_nacedora_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Elimina un datos_sensores_nacedora existente
"""
@datos_sensores_nacedora.route('/datos_sensores_nacedoras/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "datos_sensores_nacedora eliminado correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar el datos_sensores_nacedora"
    return jsonify(msg), 204