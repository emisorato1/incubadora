from app import db 
from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class TipoSensor(db.Model):
    __tablename__= 'tipo_sensor'
    
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo_sensor: str = db.Column(db.String, nullable=False)

    # Definición de la relación "uno a muchos" con datos_sensores_incubadora
    datos_sensor_incubadora = db.relationship('DatosSensorIncubadora', back_populates='tipo_sensor')
    
    # Definición de la relación "uno a muchos" con datos_sensores_nacedora
    datos_sensor_nacedora = db.relationship('DatosSensorNacedora', back_populates='tipo_sensor')
    
    def __init__(self, tipo_sensor: str = None):
        self.tipo_sensor = tipo_sensor