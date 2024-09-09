from app import db 
from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class TipoHuevo(db.Model):
    __tablename__= 'tipo_huevo'
    
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo_huevo: str = db.Column(db.String, nullable=False)
    
    # Definición de la relación "uno a muchos" con detalles_nacimiento
    detalles_nacimiento = db.relationship('DetallesNacimiento', back_populates='tipo_huevo')
    
    # Definición de la relación "uno a muchos" con detalles_incubacion
    detalles_incubacion = db.relationship('DetallesIncubacion', back_populates='tipo_huevo')
    
    def __init__(self, tipo_huevo: str = None):
        self.tipo_huevo = tipo_huevo
