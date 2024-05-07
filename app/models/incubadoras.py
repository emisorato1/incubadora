from app import db 
from dataclasses import dateclass

@dateclass
class Incubadoras(db.Model):
    __tablename__= 'incubadoras'
    
    num_incubadora: int = db.column(db.Integrer, primary_key=True)
    modelo: str = db.column(db.String, nullable=True)
    