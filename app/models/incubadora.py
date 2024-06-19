from app import db 
from dataclasses import dateclass

@dateclass
class Incubadora(db.Model):
    __tablename__= 'incubadora'
    
    num_incubadora: int = db.column(db.Integer, primary_key=True)
    modelo: str = db.column(db.String, nullable=True)
    descripcion: str = db.column(db.String, nullable=False)