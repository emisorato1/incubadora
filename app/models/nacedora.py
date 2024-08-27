from app import db 
from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class Nacedora(db.Model):
    __tablename__= 'nacedora'
    
    id: int = db.Column(db.Integer, primary_key=True)
    modelo: str = db.Column(db.String, nullable=False)
    
    # Definición de la relación "uno a muchos" con nacimiento
    nacimiento = db.relationship('Nacimiento', back_populates='nacedora')
        
    def __init__(self, modelo: int = None):
        self.modelo = modelo