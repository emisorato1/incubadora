from app import db 
from dataclasses import dataclass
from datetime import datetime

@dataclass(init=False, repr=True, eq=True)
class Datos_sensores_nacedora(db.Model):
    __tablename__= 'datos_sensores_nacedora'
    
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    valor: int = db.Column(db.Integer, nullable=False)
    dia: datetime = db.Column(db.DateTime, nullable=False)
    
    # Definición de la relación "uno a muchos" con nacimiento    
    nacimiento_id = db.Column(db.Integer, db.ForeignKey('nacimiento.id'), nullable=True)
    nacimiento = db.relationship('Nacimiento', back_populates='datos_sensores_nacedora')
    
    # Definición de la relación "uno a muchos" con tipo_sensor    
    tipo_sensor_id = db.Column(db.Integer, db.ForeignKey('tipo_sensor.id'), nullable=True)
    tipo_sensor = db.relationship('Tipo_sensor', back_populates='datos_sensores_nacedora')
    
    def __init__(self, valor: int = None, dia: datetime = None, nacimiento: int = None, tipo_sensor: int = None):
        self.valor = valor
        self.dia = dia
        self.nacimiento = nacimiento
        self.tipo_sensor = tipo_sensor