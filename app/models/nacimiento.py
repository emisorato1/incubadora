from app import db
from dataclasses import dataclass
from datetime import datetime


@dataclass(init=False, repr=True, eq=True)
class Nacimiento(db.Model):
    __tablename__= 'nacimiento'
    
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha_entrada_inc: datetime = db.Column(db.DateTime, nullable=True)
    fecha_salida_inc: datetime = db.Column(db.DateTime, nullable=False)
    
    # Definición de la relación "uno a muchos" con User    
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='proceso')
    
    # Definición de la relación "uno a muchos" con incubadora
    nacedora_id = db.Column('nacedora_id', db.Integer, db.ForeignKey('incubadora.id'), nullable=False)
    nacedora = db.relationship('Nacedora', back_populates='nacimiento')
    
    def __init__(self, fecha_entrada: datetime = None, fecha_salida: datetime = None, user: int = None, nacedora: int = None):
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.user = user
        self.nacedora = nacedora