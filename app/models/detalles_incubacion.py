from app import db
from dataclasses import dataclass

@dataclass
class Detalles_incubacion(db.Model):
    __tablename__= 'detalles_incubacion'
    
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cant_huevos_inicial: int = db.Column(db.Integer, nullable=False) 
    cant_huevos_final: int = db.Column(db.Integer, nullable=False) 

    # Definición de la relación "uno a muchos" con incubadora    
    incubacion_id = db.Column('incubacion_id', db.Integer, db.Foreignkey('incubacion.id'))
    incubacion = db.relationship('Incubacion', back_populates='detalles_incubacion')
    
    # Definición de la relación "uno a muchos" con tipo_huevo    
    tipo_huevo_id = db.Column('tipo_huevo_id', db.Integer, db.Foreignkey('tipo_huevo.id'))
    tipo_huevo = db.relationship('Tipo_huevo', back_populates='detalles_incubacion')
    
    def __init__(self, cant_huevos_inicial: int = None, cant_huevos_final: int = None, incubacion: int = None, tipo_huevo: int = None):
        self.cant_huevos_inicial = cant_huevos_inicial
        self.cant_huevos_final = cant_huevos_final
        self.incubacion = incubacion
        self.tipo_huevo = tipo_huevo
    