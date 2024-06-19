from app import db 
from dataclasses import dataclass
from typing import List

from .proceso import Proceso

@dataclass
class User(db.Model):
    __tablename__= 'user'
    
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name: str = db.Column(db.String, nullable=True)
    password: str = db.Column(db.String(120), nullable=False)
    role: str = db.Column(db.String, nullable=True)
    
    # Definición de la relación "uno a muchos" con proceso    
    proceso_id = db.Column('proceso_id', db.Integer, db.Foreignkey('proceso.id'))
    proceso = db.relationship('Proceso', back_populates='user')
    
    