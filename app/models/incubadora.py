from app import db 
from dataclasses import dateclass

@dateclass(init=False, repr=True, eq=True)
class Incubadora(db.Model):
    __tablename__= 'incubadora'
    
    id: int = db.column(db.Integer, primary_key=True)
    modelo: str = db.column(db.String, nullable=True)
    
    def __init__(self, modelo: int = None):
        self.modelo = modelo