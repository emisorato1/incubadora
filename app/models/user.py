from app import db 
from dataclasses import dataclass
from typing import List

@dataclass(init=False, repr=True, eq=True)
class User(db.Model):
    __tablename__= 'user'
    
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name: str = db.Column(db.String(120), nullable=True)
    password: str = db.Column(db.String(120), nullable=True)
    role: str = db.Column(db.String, nullable=True)
    
    def __init__(self, user_name: str = None, password: str = None, role: str = None):
        self.user_name = user_name
        self.password = password
        self.role = role
    