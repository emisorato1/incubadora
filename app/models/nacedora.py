from app import db 
from dataclasses import dateclass

@dateclass
class Nacedora(db.Model):
    __tablename__= 'nacedora'
    
    num_nacedora: int = db.column(db.Integer, primary_key=True)
    modelo: str = db.column(db.String, nullable=True)
    descripcion: str = db.column(db.String, nullable=False)