from app import db 
from dataclasses import dateclass

@dateclass
class Sensores(db.Model):
    __tablename__= 'sensores_incubadora'
    
    id: int = db.column(db.Integrer, primary_key=True)
    motor_volteado: str = db.column(db.String, nullable=True)
    ventilacion: str = db.column(db.String, nullable=True) # va a decir si esta en funcionamiento o no
    temperatura: int = db.column(db.Integrer, nullable=True) # va a decir la temperatura en ese momento
    humedad: int = db.column(db.Integrer, nullable=True) # va a decir la humedad en ese momento
    resistencia: str = db.column(db.String, nullable=True)