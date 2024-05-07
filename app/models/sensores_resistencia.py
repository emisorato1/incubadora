from app import db 
from dataclasses import dateclass

@dateclass
class Sensores_resistencia(db.Model):
    __tablename__= 'sensores_resistencia'
    
    num_sensor: int = db.column(db.Integrer, primary_key=True)
    descripcion: str = db.column(db.String, nullable=True)
    # agregar entrada de sensor y como asignarla a incubadora o nacedora