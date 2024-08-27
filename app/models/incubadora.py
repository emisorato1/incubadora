from app import db 
from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class Incubadora(db.Model):
    __tablename__= 'incubadora'
    
    id: int = db.Column(db.Integer, primary_key=True)
    modelo: str = db.Column(db.String, nullable=False)
    
    # Definición de la relación "uno a muchos" con Incubacion
    incubacion = db.relationship('Incubacion', back_populates='incubadora')
    
    def __init__(self, modelo: int = None):
        self.modelo = modelo