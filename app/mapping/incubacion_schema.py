from marshmallow import Schema, fields, post_load
from app.models import Incubacion

# Define el esquema (Schema) para la clase Incubacion
class IncubacionSchema(Schema):
    # Define campos del esquema y establece reglas de validación y serialización

    id = fields.Integer(dump_only=True)  # Campo 'id' de tipo Integer (solo para volcado/serialización)
    fecha_entrada = fields.DateTime(required=True)  
    fecha_salida = fields.DateTime(required=False) 
    
    # Método para manejar la carga de datos (deserialización)
    @post_load
    def make_incubacion(self, data, **kwargs):
        return Incubacion(**data)  # Crea una instancia de la clase Usuario con los datos deserializados