from app import db 
from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class Tipo_huevo(db.Model):
    __tablename__= 'tipo_huevo'
    
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo_huevo: str = db.Column(db.String, nullable=False)
    
    # Definición de la relación "uno a muchos" con detalles_nacimiento
    detalles_nacimiento = db.relationship('Detalles_nacimiento', back_populates='tipo_huevo')
    
    # Definición de la relación "uno a muchos" con detalles_incubacion
    detalles_incubacion = db.relationship('Detalles_incubacion', back_populates='tipo_huevo')
    
    def __init__(self, tipo_huevo: str = None):
        self.tipo_huevo = tipo_huevo
