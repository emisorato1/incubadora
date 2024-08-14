from app import db
from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass(init=False, repr=True, eq=True)
class Incubacion(db.Model):
    __tablename__= 'incubacion'
    
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha_entrada: datetime = db.Column(db.DateTime, nullable=True)
    fecha_salida: datetime = db.Column(db.DateTime, nullable=False)
    
    # Definición de la relación "uno a muchos" con User    
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='incubacion')
    
    # Definición de la relación "uno a muchos" con incubadora    
    incubadora_id = db.Column('incubadora_id', db.Integer, db.ForeignKey('incubadora.id'), nullable=False)
    incubadora = db.relationship('Incubadora', back_populates='incubacion')
    
    def __init__(self, fecha_entrada: datetime = None, fecha_salida: datetime = None, user: int = None, incubadora: int = None):
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.user = user
        self.incubadora = incubadora
    
    