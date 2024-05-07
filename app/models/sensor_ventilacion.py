from app import db 
from dataclasses import dateclass

@dateclass
class Sensor_ventilacion(db.Model):
    __tablename__= 'sensor_ventilacion'
    
    num_sensor: int = db.column(db.Integrer, primary_key=True)
    descripcion: str = db.column(db.String, nullable=True)
    # agregar entrada de sensor y como asignarla a incubadora o nacedora