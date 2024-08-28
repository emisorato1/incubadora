from flask import jsonify, Blueprint, request
from app.mapping import Datos_sensores_incubadoraSchema
from app.services.datos_sensores_incubadora_services import Datos_sensores_incubadoraService

datos_sensores_incubadora = Blueprint('datos_sensores_incubadora', __name__)
service = Datos_sensores_incubadoraService()
datos_sensores_incubadora_schema = Datos_sensores_incubadoraSchema()

"""
Obtiene todos los datos_sensores_incubadoras
"""
@datos_sensores_incubadora.route('/datos_sensores_incubadora', methods=['GET'])
def all():
    resp = datos_sensores_incubadora_schema.dump(service.get_all(), many=True) 
    return resp, 200

"""
Obtiene una datos_sensores_incubadoras por id
"""
@datos_sensores_incubadora.route('/datos_sensores_incubadoras/<int:id>', methods=['GET'])
def one(id):
    resp = datos_sensores_incubadora_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Elimina un datos_sensores_incubadora existente
"""
@datos_sensores_incubadora.route('/datos_sensores_incubadoras/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "datos_sensores_incubadora eliminado correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar el datos_sensores_incubadora"
    return jsonify(msg), 204