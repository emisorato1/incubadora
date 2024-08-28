from app.models import Tipo_sensor
from app import db
from .repository import Repository_get, Repository_create, Repository_update, Repository_delete


class Tipo_sensorRepository(Repository_get,Repository_create,Repository_update,Repository_delete):  
     def __init__(self):
         self.__model = Tipo_sensor

     def get_all(self) -> list[Tipo_sensor]:
        return db.session.query(self.__model).all()
        
     def get_by_id(self, id) -> Tipo_sensor:
         return db.session.query(self.__model).get(id)
     
     def create(self, entity: Tipo_sensor) -> Tipo_sensor:
         db.session.add(entity)
         db.session.commit()
         return entity
         
     def update(self, id, t: Tipo_sensor) -> Tipo_sensor:
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