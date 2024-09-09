from app.models import TipoSensor
from app import db
from .repository import Repository_get, Repository_create, Repository_update, Repository_delete


class TipoSensorRepository(Repository_get,Repository_create,Repository_update,Repository_delete):  
     def __init__(self):
         self.__model = TipoSensor

     def get_all(self) -> list[TipoSensor]:
        return db.session.query(self.__model).all()
        
     def get_by_id(self, id) -> TipoSensor:
         return db.session.query(self.__model).get(id)
     
     def create(self, entity: TipoSensor) -> TipoSensor:
         db.session.add(entity)
         db.session.commit()
         return entity
         
     def update(self, id, t: TipoSensor) -> TipoSensor:
         entity = self.get_by_id(id)
         if entity:
             entity.tipo_sensor=t.tipo_sensor
             db.session.add(entity)
             db.session.commit()
             return entity
         return None
         
     def delete(self, id)-> bool:
         tipo_sensor = self.get_by_id(id)
         if tipo_sensor:
             db.session.delete(tipo_sensor)
             db.session.commit()
             return True
         return False