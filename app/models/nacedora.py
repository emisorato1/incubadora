from app import db 
from dataclasses import dateclass

@dateclass(init=False, repr=True, eq=True)
class Nacedora(db.Model):
    __tablename__= 'nacedora'
    
    id: int = db.column(db.Integer, primary_key=True)
    modelo: str = db.column(db.String, nullable=True)
    descripcion: str = db.column(db.String, nullable=False)
    
    def __init__(self, modelo: int = None):
        self.modelo = modelo