from flask import jsonify, Blueprint, request
from app.mapping import NacedoraSchema
from app.services.nacedora_services import NacedoraService

nacedora = Blueprint('nacedora', __name__)
service = NacedoraService()
nacedora_schema = NacedoraSchema()

"""
Obtiene todos las nacedoras
"""
@nacedora.route('/nacedora', methods=['GET'])
def all():
    resp = nacedora_schema.dump(service.get_all(), many=True) 
    return resp, 200

"""
Obtiene una nacedoras por id
"""
@nacedora.route('/nacedoras/<int:id>', methods=['GET'])
def one(id):
    resp = nacedora_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Crea nueva nacedora
"""
@nacedora.route('/nacedoras', methods=['POST'])
def create():
    usuario = nacedora_schema.load(request.json)
    resp = nacedora_schema.dump(service.create(usuario))
    return resp, 201

"""
Elimina una nacedora existente
"""
@nacedora.route('/nacedoras/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "nacedora eliminada correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar la incubadora"
    return jsonify(msg), 204