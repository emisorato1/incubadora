from app import db 
from dataclasses import dateclass

@dateclass
class Datos_sensores_nacedoras(db.Model):
    __tablename__= 'datos_sensores_nacedoras'
    
    id: int = db.column(db.Integrer, primary_key=True)
    ventilacion: str = db.column(db.String, nullable=True) # va a decir si esta en funcionamiento o no
    temperatura: int = db.column(db.Integrer, nullable=True) # va a decir la temperatura en ese momento
    humedad: int = db.column(db.Integrer, nullable=True) # va a decir la humedad en ese momento
    resistencia: str = db.column(db.String, nullable=True) # va a decir la temperatura en ese momento