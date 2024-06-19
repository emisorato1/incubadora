from app import db 
from dataclasses import dateclass

@dateclass
class Sensores(db.Model):
    __tablename__= 'sensores'
    
    id: int = db.column(db.Integer, primary_key=True, autoincrement=True)
    tipo_sensor: str = db.column(db.String, nullable=True)
    medicion: str = db.column(db.String, nullable=True)
    descripcion: str = db.column(db.String, nullable=True)

    