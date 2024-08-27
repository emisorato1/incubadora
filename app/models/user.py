from app import db 
from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class User(db.Model):
    __tablename__= 'user'
    
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name: str = db.Column(db.String(120), nullable=False)
    password: str = db.Column(db.String(120), nullable=False)
    role: str = db.Column(db.String, nullable=False)
    
    # Definición de la relación "uno a muchos" con Incubacion
    incubacion = db.relationship('Incubacion', back_populates='user')
    
    # Definición de la relación "uno a muchos" con nacimiento
    nacimiento = db.relationship('Nacimiento', back_populates='user')
    
    def __init__(self, user_name: str = None, password: str = None, role: str = None):
        self.user_name = user_name
        self.password = password
        self.role = role
    