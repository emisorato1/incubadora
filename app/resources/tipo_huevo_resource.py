from flask import jsonify, Blueprint, request
from app.mapping import Tipo_huevoSchema
from app.services.tipo_huevo_services import Tipo_huevoService

tipo_huevo = Blueprint('Tipo_huevo', __name__)
service = Tipo_huevoService()
tipo_huevo_schema = Tipo_huevoSchema()

"""
Obtiene todos los Tipo_huevos
"""
@tipo_huevo.route('/Tipo_huevo', methods=['GET'])
def all():
    resp = tipo_huevo_schema.dump(service.get_all(), many=True) 
    return resp, 200

"""
Obtiene una Tipo_huevos por id
"""
@tipo_huevo.route('/Tipo_huevos/<int:id>', methods=['GET'])
def one(id):
    resp = tipo_huevo_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Crea nuevo Tipo_huevo
"""
@tipo_huevo.route('/Tipo_huevos', methods=['POST'])
def create():
    tipo_huevo = tipo_huevo_schema.load(request.json)
    resp = tipo_huevo_schema.dump(service.create(tipo_huevo))
    return resp, 201

"""
Elimina un Tipo_huevo existente
"""
@tipo_huevo.route('/Tipo_huevo++++++++++++++++++++++++++s/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "Tipo_huevo eliminado correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar el Tipo_huevo"
    return jsonify(msg), 204