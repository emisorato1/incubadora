from app import db 
from dataclasses import dateclass
from datetime import datetime

@dateclass(init=False, repr=True, eq=True)
class Datos_sensores_incubadora(db.Model):
    __tablename__= 'datos_sensores_incubadora'
    
    id: int = db.column(db.Integer, primary_key=True, autoincrement=True)
    valor: int = db.Column(db.Integer, nullable=True)
    dia: datetime = db.Column(db.DateTime, nullable=True)
    
    # Definición de la relación "uno a muchos" con incubadora    
    incubacion_id = db.Column('incubacion_id', db.Integer, db.ForeignKey('incubacion.id'), nullable=False)
    incubacion = db.relationship('Incubacion', back_populates='datos_sensores_incubadora')
    
    # Definición de la relación "uno a muchos" con tipo_sensor    
    tipo_sensor_id = db.Column('tipo_sensor_id', db.Integer, db.ForeignKey('tipo_sensor.id'), nullable=False)
    tipo_sensor = db.relationship('Tipo_sensor', back_populates='datos_sensores_incubadora')
    
    def __init__(self, valor: int = None, dia: datetime = None, incubacion: int = None, tipo_sensor: int = None):
        self.valor = valor
        self.dia = dia
        self.incubacion = incubacion
        self.tipo_sensor = tipo_sensor