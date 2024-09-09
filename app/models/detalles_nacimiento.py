from app import db
from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class DetallesNacimiento(db.Model):
    __tablename__= 'detalles_nacimiento'
    
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cant_huevos_inicial: int = db.Column(db.Integer, nullable=False) 
    cant_huevos_final: int = db.Column(db.Integer, nullable=True) 

    # Definición de la relación "uno a muchos" con nacimiento    
    nacimiento_id = db.Column(db.Integer, db.ForeignKey('nacimiento.id'), nullable=True)
    nacimiento = db.relationship('Nacimiento', back_populates='detalles_nacimiento')
    
    # Definición de la relación "uno a muchos" con tipo_huevo    
    tipo_huevo_id = db.Column(db.Integer, db.ForeignKey('tipo_huevo.id'), nullable=True)
    tipo_huevo = db.relationship('TipoHuevo', back_populates='detalles_nacimiento')
    
    def __init__(self, cant_huevos_inicial: int = None, cant_huevos_final: int = None, nacimiento: int = None, tipo_huevo: int = None):
        self.cant_huevos_inicial = cant_huevos_inicial
        self.cant_huevos_final = cant_huevos_final
        self.nacimiento = nacimiento
        self.tipo_huevo = tipo_huevo