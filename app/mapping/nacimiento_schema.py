from marshmallow import Schema, fields, post_load
from app.models import Nacimiento

# Define el esquema (Schema) para la clase Nacimiento
class NacimientoSchema(Schema):
    # Define campos del esquema y establece reglas de validación y serialización

    id = fields.Integer(dump_only=True)  # Campo 'id' de tipo Integer (solo para volcado/serialización)
    fecha_entrada = fields.DateTime(required=True)  
    fecha_salida = fields.DateTime(required=False) 
    
    # Método para manejar la carga de datos (deserialización)
    @post_load
    def make_nacimiento(self, data, **kwargs):
        return Nacimiento(**data)  # Crea una instancia de la clase Usuario con los datos deserializados