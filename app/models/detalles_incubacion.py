from app import db
from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class DetallesIncubacion(db.Model):
    __tablename__= 'detalles_incubacion'
    
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cant_huevos_inicial: int = db.Column(db.Integer, nullable=False) 
    cant_huevos_final: int = db.Column(db.Integer, nullable=True) 

    # Definición de la relación "uno a muchos" con incubacion    
    incubacion_id = db.Column(db.Integer, db.ForeignKey('incubacion.id'), nullable=True)
    incubacion = db.relationship('Incubacion', back_populates='detalles_incubacion')
    
    # Definición de la relación "uno a muchos" con tipo_huevo    
    tipo_huevo_id = db.Column(db.Integer, db.ForeignKey('tipo_huevo.id'), nullable=True)
    tipo_huevo = db.relationship('TipoHuevo', back_populates='detalles_incubacion')
    
    def __init__(self, cant_huevos_inicial: int = None, cant_huevos_final: int = None, incubacion: int = None, tipo_huevo: int = None):
        self.cant_huevos_inicial = cant_huevos_inicial
        self.cant_huevos_final = cant_huevos_final
        self.incubacion = incubacion
        self.tipo_huevo = tipo_huevo
    