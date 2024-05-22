from app import db
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Proceso(db.Model):
    __tablename__= 'proceso'
    
    id: int = db.column(db.Integrer, primary_key=True, autoincrement=True)
    incubadora_asignada: int = db.Column(db.Integrer, nullable=True)
    fecha_entrada_inc: datetime = db.Column(db.DateTime, nullable=True)
    ent_araucana: int = db.Column(db.Integrer, nullable=True) # cantidad de araucanas entrantes
    ent_camperos: int = db.Column(db.Integrer, nullable=True) # cantidad de camperos entrantes
    ent_belichas: int = db.Column(db.Integrer, nullable=True) # cantidad de belichas entrantes
    fecha_salida_inc: datetime = db.Column(db.DateTime, nullable=False)
    fert_araucanas: int = db.Column(db.Integrer, nullable=False) # cantidad de huevos fertiles de araucana
    fert_camperos: int = db.Column(db.Integrer, nullable=False) # cantidad de huevos fertiles de camperos
    fert_belichas: int = db.Column(db.Integrer, nullable=False) # cantidad de huevos fertiles de belichas
    nacedora_asignada: int = db.Column(db.Integrer, nullable=False)
    fecha_entrada_nac: datetime = db.Column(db.DateTime, nullable=False)
    fecha_salida_nac: datetime = db.Column(db.DateTime, nullable=False)
    nac_araucana: int = db.Column(db.Integrer, nullable=False) # cantidad de nacimientos de araucana
    nac_camperos: int = db.Column(db.Integrer, nullable=False) # cantidad de nacimientos de camperos
    nac_belichas: int = db.Column(db.Integrer, nullable=False) # cantidad de nacimientos de belichas
    detalles: str = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Proceso %r>' % self.incubadora_asignada
