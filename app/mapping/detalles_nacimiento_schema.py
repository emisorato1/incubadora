from marshmallow import Schema, fields, post_load
from app.models import Detalles_nacimiento

# Define el esquema (Schema) para la clase Detalle_nacimiento
class Detalles_nacimientoSchema(Schema):
    # Define campos del esquema y establece reglas de validación y serialización

    id = fields.Integer(dump_only=True)  # Campo 'id' de tipo Integer (solo para volcado/serialización)
    cant_huevos_inicial = fields.Integer(required=True)  
    cant_huevos_final = fields.Integer(required=False) 
    
    # Método para manejar la carga de datos (deserialización)
    @post_load
    def make_detalle_nacimiento(self, data, **kwargs):
        return Detalles_nacimiento(**data)  # Crea una instancia de la clase Usuario con los datos deserializados