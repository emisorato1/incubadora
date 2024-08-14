from app import db 
from dataclasses import dateclass

@dateclass(init=False, repr=True, eq=True)
class Tipo_sensor(db.Model):
    __tablename__= 'tipo_sensor'
    
    id: int = db.column(db.Integer, primary_key=True, autoincrement=True)
    tipo_huevo: str = db.column(db.String, nullable=True)
    
    def __init__(self, tipo_huevo: str = None):
        self.tipo_huevo = tipo_huevo
