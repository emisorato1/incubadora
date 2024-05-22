from app import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Proceso(db.Model):
    __tablename__= 'proceso'
    
    id: int = db.column(db.Integrer, primary_key=True, autoincrement=True)
    
    # Relación unidireccional "uno a uno" con incubarora
    incubadora_id = db.Column(db.Integer, db.ForeignKey('incubadora.id'))
    incubadora_asignada = db.relationship('Incubadora', uselist=False)

    #Proceso de incubadora
    fecha_entrada_inc: datetime = db.Column(db.DateTime, nullable=True)
    ent_araucana: int = db.Column(db.Integrer, nullable=True) # cantidad de araucanas entrantes
    ent_camperos: int = db.Column(db.Integrer, nullable=True) # cantidad de camperos entrantes
    ent_belichas: int = db.Column(db.Integrer, nullable=True) # cantidad de belichas entrantes
    fecha_salida_inc: datetime = db.Column(db.DateTime, nullable=False)
    fert_araucanas: int = db.Column(db.Integrer, nullable=False) # cantidad de huevos fertiles de araucana
    fert_camperos: int = db.Column(db.Integrer, nullable=False) # cantidad de huevos fertiles de camperos
    fert_belichas: int = db.Column(db.Integrer, nullable=False) # cantidad de huevos fertiles de belichas
    
    # Relación unidireccional "uno a uno" con nacedora
    nacedora_id = db.Column(db.Integer, db.ForeignKey('nacedora.id'))
    nacedora_asignada = db.relationship('Nacedora', uselist=False)

    # Proceso nacedora
    fecha_entrada_nac: datetime = db.Column(db.DateTime, nullable=False)
    fecha_salida_nac: datetime = db.Column(db.DateTime, nullable=False)
    nac_araucana: int = db.Column(db.Integrer, nullable=False) # cantidad de nacimientos de araucana
    nac_camperos: int = db.Column(db.Integrer, nullable=False) # cantidad de nacimientos de camperos
    nac_belichas: int = db.Column(db.Integrer, nullable=False) # cantidad de nacimientos de belichas
    detalles: str = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return '<Proceso %r>' % self.incubadora_asignada
