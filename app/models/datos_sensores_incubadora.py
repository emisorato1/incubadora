from app import db 
from dataclasses import dateclass

@dateclass
class Datos_sensores_incubadora(db.Model):
    __tablename__= 'datos_sensores_incubadora'
    
    id: int = db.column(db.Integrer, primary_key=True)
    motor_volteado: str = db.column(db.String, nullable=True) # va a decir la temperatura en ese momento
    ventilacion: str = db.column(db.String, nullable=True) # va a decir si esta en funcionamiento o no
    temperatura: int = db.column(db.Integrer, nullable=True) # va a decir la temperatura en ese momento
    humedad: int = db.column(db.Integrer, nullable=True) # va a decir la humedad en ese momento
    resistencia: str = db.column(db.String, nullable=True) # va a decir la temperatura en ese momento