from flask import jsonify, Blueprint, request
from app.mapping import Tipo_sensorSchema
from app.services.tipo_sensor_services import Tipo_sensorService

tipo_sensor = Blueprint('Tipo_sensor', __name__)
service = Tipo_sensorService()
tipo_sensor_schema = Tipo_sensorSchema()

"""
Obtiene todos los Tipo_sensores
"""
@tipo_sensor.route('/Tipo_sensor', methods=['GET'])
def all():
    resp = tipo_sensor_schema.dump(service.get_all(), many=True) 
    return resp, 200

"""
Obtiene una Tipo_sensores por id
"""
@tipo_sensor.route('/Tipo_sensores/<int:id>', methods=['GET'])
def one(id):
    resp = tipo_sensor_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Crea nuevo Tipo_sensor
"""
@tipo_sensor.route('/Tipo_sensores', methods=['POST'])
def create():
    tipo_sensor = tipo_sensor_schema.load(request.json)
    resp = tipo_sensor_schema.dump(service.create(tipo_sensor))
    return resp, 201

"""
Elimina un Tipo_sensor existente
"""
@tipo_sensor.route('/Tipo_sensores/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "Tipo_sensor eliminado correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar el Tipo_sensor"
    return jsonify(msg), 204