from app import db 
from dataclasses import dataclass
from datetime import datetime

@dataclass(init=False, repr=True, eq=True)
class DatosSensorIncubadora(db.Model):
    __tablename__= 'datos_sensor_incubadora'
    
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    valor: int = db.Column(db.Integer, nullable=False)
    dia: datetime = db.Column(db.DateTime, nullable=False)
    
    # Definición de la relación "uno a muchos" con incubacion    
    incubacion_id = db.Column(db.Integer, db.ForeignKey('incubacion.id'), nullable=True)
    incubacion = db.relationship('Incubacion', back_populates='datos_sensor_incubadora')
    
    # Definición de la relación "uno a muchos" con tipo_sensor    
    tipo_sensor_id = db.Column(db.Integer, db.ForeignKey('tipo_sensor.id'), nullable=True)
    tipo_sensor = db.relationship('TipoSensor', back_populates='datos_sensor_incubadora')
    
    
    def __init__(self, valor: int = None, dia: datetime = None, incubacion: int = None, tipo_sensor: int = None):
        self.valor = valor
        self.dia = dia
        self.incubacion = incubacion
        self.tipo_sensor = tipo_sensor