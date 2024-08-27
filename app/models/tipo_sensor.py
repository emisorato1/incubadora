from app import db 
from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class Tipo_sensor(db.Model):
    __tablename__= 'tipo_sensor'
    
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo_sensor: str = db.Column(db.String, nullable=False)

    # Definición de la relación "uno a muchos" con datos_sensores_incubadora
    datos_sensores_incubadora = db.relationship('Datos_sensores_incubadora', back_populates='tipo_sensor')
    
    # Definición de la relación "uno a muchos" con datos_sensores_nacedora
    datos_sensores_nacedora = db.relationship('Datos_sensores_nacedora', back_populates='tipo_sensor')
    
    def __init__(self, tipo_sensor: str = None):
        self.tipo_sensor = tipo_sensor