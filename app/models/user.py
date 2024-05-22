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
    
    def __repr__(self):
        return '<User %r>' % self.user_name
        