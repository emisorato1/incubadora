from app import db 
from dataclasses import dateclass

@dateclass
class Tipo_ensor(db.Model):
    __tablename__= 'tipo_sensor'
    
    id: int = db.column(db.Integer, primary_key=True, autoincrement=True)
    tipo_sensor: str = db.column(db.String, nullable=True)

    def __init__(self, tipo_sensor: str = None):
        self.tipo_sensor = tipo_sensor