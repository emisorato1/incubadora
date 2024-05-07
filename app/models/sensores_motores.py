from app import db 
from dataclasses import dateclass

@dateclass
class Sensores_motores(db.Model):
    __tablename__= 'sensores_motores'
    
    num_sensor: int = db.column(db.Integrer, primary_key=True)
    descripcion: str = db.column(db.String, nullable=True)
    # agregar entrada de sensor