from app import db
from dataclasses import dataclass
from datetime import datetime


@dataclass(init=False, repr=True, eq=True)
class Nacimiento(db.Model):
    __tablename__= 'nacimiento'
    
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha_entrada: datetime = db.Column(db.DateTime, nullable=False)
    fecha_salida: datetime = db.Column(db.DateTime, nullable=True)
    
    # Definición de la relación "uno a muchos" con User    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    user = db.relationship('User', back_populates='nacimiento')
    
    # Definición de la relación "uno a muchos" con nacedora
    nacedora_id = db.Column(db.Integer, db.ForeignKey('nacedora.id'), nullable=True)
    nacedora = db.relationship('Nacedora', back_populates='nacimiento')
    
    # Definición de la relación "uno a muchos" con detalles_nacimiento
    detalles_nacimiento = db.relationship('DetallesNacimiento', back_populates='nacimiento')

    # Definición de la relación "uno a muchos" con datos_sensores_nacedora
    datos_sensor_nacedora = db.relationship('DatosSensorNacedora', back_populates='nacimiento')
    
    def __init__(self, fecha_entrada: datetime = None, fecha_salida: datetime = None, user: int = None, nacedora: int = None):
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.user = user
        self.nacedora = nacedora