from marshmallow import Schema, fields, post_load
from app.models import Nacedora

# Define el esquema (Schema) para la clase Nacedora
class NacedoraSchema(Schema):
    # Define campos del esquema y establece reglas de validación y serialización

    id = fields.Integer(dump_only=True)  # Campo 'id' de tipo Integer (solo para volcado/serialización)
    modelo = fields.String(required=True)  
    
    # Método para manejar la carga de datos (deserialización)
    @post_load
    def make_nacedora(self, data, **kwargs):
        return Nacedora(**data)  # Crea una instancia de la clase Usuario con los datos deserializados