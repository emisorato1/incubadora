from app import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Datos_nacedora(db.Model):
    __tablename__= 'datos_nacedora'
    
    id: int = db.column(db.Integrer, primary_key=True, autoincrement=True)
    nacedora_asignada: int
    dias: datetime = db.column(db.DateTime, nullable=False, default=datetime)
    fecha_entrada: datetime = db.column(db.DateTime, nullable=False)
    fecha_salida: datetime = db.column(db.DateTime, nullable=False)
    fertilidad: int = db.clolumn(db.Integrer, nullable=True)
    tipo_gallina_1: int = db.calumn(db.Integrer, nullable=True)
    tipo_gallina_2: int = db.calumn(db.Integrer, nullable=True)
    tipo_gallina_3: int = db.calumn(db.Integrer, nullable=True)