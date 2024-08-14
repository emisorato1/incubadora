from marshmallow import validate, Schema, fields, post_load
from app.models import User

# Define el esquema (Schema) para la clase Usuario
class UserSchema(Schema):
    # Define campos del esquema y establece reglas de validación y serialización

    id = fields.Integer(dump_only=True)  # Campo 'id' de tipo Integer (solo para volcado/serialización)
    user_name = fields.String(required=True, validate=validate.Length(min=2, max=120))  
    role = fields.String(required=True) 
    password = fields.String(load_only=True)  # Campo 'password' de tipo String (solo para carga/deserialización)

    # Método para manejar la carga de datos (deserialización)
    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)  # Crea una instancia de la clase Usuario con los datos deserializados