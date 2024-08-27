from marshmallow import validate, Schema, fields, post_load
from app.models.tipo_sensor import Tipo_sensor

# Define el esquema (Schema) para la clase Tipo_sensor
class Tipo_sensorSchema(Schema):
    # Define campos del esquema y establece reglas de validación y serialización

    id = fields.Integer(dump_only=True)  # Campo 'id' de tipo Integer (solo para volcado/serialización)
    tipo_sensor = fields.String(required=True, validate=validate.Length(min=2, max=120))  
    
    # Método para manejar la carga de datos (deserialización)
    @post_load
    def make_tipo_sensor(self, data, **kwargs):
        return Tipo_sensor(**data)  # Crea una instancia de la clase Usuario con los datos deserializados