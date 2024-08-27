from marshmallow import Schema, fields, post_load
from app.models.datos_sensores_incubadora import Datos_sensores_incubadora

# Define el esquema (Schema) para la clase Datos_sensores_incubadora
class Datos_sensores_incubadoraSchema(Schema):
    # Define campos del esquema y establece reglas de validación y serialización

    id = fields.Integer(dump_only=True)  # Campo 'id' de tipo Integer (solo para volcado/serialización)
    valor = fields.Integer(required=True)  
    dia = fields.DateTime(required=True) 
    
    # Método para manejar la carga de datos (deserialización)
    @post_load
    def make_datos_sensores_incubadora(self, data, **kwargs):
        return Datos_sensores_incubadora(**data)  # Crea una instancia de la clase Usuario con los datos deserializados