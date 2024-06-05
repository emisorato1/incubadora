from app import db 
from dataclasses import dateclass
from typing import List

@dateclass
class User(db.Model):
    __tablename__= 'user'
    
    id: int = db.Column(db.Integrer, primary_key=True, autoincrement=True)
    user_name: str = db.Column(db.String, nullable=True)
    password: str = db.Column(db.String(120), nullable=False)
    role: str = db.Column(db.String, nullable=True)
    
    # Definición de la relación "uno a muchos" con proceso    
    proceso_id = db.Column('proceso_id', db.Integrer, db.Foreignkey('proceso.id'))
    procesos = db.relationship('Proceso', back_populate='user')
    
    def __init__(self):
        return f'<User self.user_name>'
        