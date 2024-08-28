from flask import jsonify, Blueprint, request
from app.mapping import IncubadoraSchema
from app.services.incubadora_sevices import IncubadoraService

incubadora = Blueprint('incubadora', __name__)
service = IncubadoraService()
incubadora_schema = IncubadoraSchema()

"""
Obtiene todos los incubadoras
"""
@incubadora.route('/incubadora', methods=['GET'])
def all():
    resp = incubadora_schema.dump(service.get_all(), many=True) 
    return resp, 200

"""
Obtiene una incubadoras por id
"""
@incubadora.route('/incubadoras/<int:id>', methods=['GET'])
def one(id):
    resp = incubadora_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Crea nuevo incubadora
"""
@incubadora.route('/incubadoras', methods=['POST'])
def create():
    incubadora = incubadora_schema.load(request.json)
    resp = incubadora_schema.dump(service.create(incubadora))
    return resp, 201

"""
Elimina una incubadora existente
"""
@incubadora.route('/incubadoras/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "incubadora eliminada correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar la incubadora"
    return jsonify(msg), 204