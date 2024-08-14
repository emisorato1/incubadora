from app import db
from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class Detalles_nacimiento(db.Model):
    __tablename__= 'detalles_nacimiento'
    
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cant_huevos_inicial: int = db.Column(db.Integer, nullable=False) 
    cant_huevos_final: int = db.Column(db.Integer, nullable=False) 

    # Definición de la relación "uno a muchos" con incubadora    
    nacimiento_id = db.Column('nacimiento_id', db.Integer, db.ForeignKey('nacimiento.id'), nullable=False)
    nacimiento = db.relationship('Nacimiento', back_populates='detalles_nacimiento')
    
    # Definición de la relación "uno a muchos" con tipo_huevo    
    tipo_huevo_id = db.Column('tipo_huevo_id', db.Integer, db.ForeignKey('tipo_huevo.id'), nullable=False)
    tipo_huevo = db.relationship('Tipo_huevo', back_populates='detalles_nacimiento')
    
    def __init__(self, cant_huevos_inicial: int = None, cant_huevos_final: int = None, nacimiento: int = None, tipo_huevo: int = None):
        self.cant_huevos_inicial = cant_huevos_inicial
        self.cant_huevos_final = cant_huevos_final
        self.nacimiento = nacimiento
        self.tipo_huevo = tipo_huevo