from app import db 
from dataclasses import dateclass
from datetime import datetime

@dateclass(init=False, repr=True, eq=True)
class Datos_sensores_nacedora(db.Model):
    __tablename__= 'datos_sensores_nacedora'
    
    id: int = db.column(db.Integer, primary_key=True, autoincrement=True)
    valor: int = db.Column(db.Integer, nullable=True)
    dia: datetime = db.Column(db.DateTime, nullable=True)
    
    # Definición de la relación "uno a muchos" con incubadora    
    nacimiento_id = db.Column('nacimiento_id', db.Integer, db.ForeignKey('incubacion.id'), nullable=False)
    nacimiento = db.relationship('Nacimiento', back_populates='datos_sensores_nacedora')
    
    # Definición de la relación "uno a muchos" con tipo_huevo    
    tipo_sensor_id = db.Column('tipo_sensor_id', db.Integer, db.ForeignKey('tipo_sensor.id'), nullable=False)
    tipo_sensor = db.relationship('Tipo_sensor', back_populates='datos_sensores_nacedora')
    
    def __init__(self, valor: int = None, dia: datetime = None, nacimiento: int = None, tipo_sensor: int = None):
        self.valor = valor
        self.dia = dia
        self.nacimiento = nacimiento
        self.tipo_sensor = tipo_sensor