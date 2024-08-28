from app.models import Datos_sensores_nacedora
from app import db
from .repository import Repository_get, Repository_create, Repository_update, Repository_delete


class Datos_sensores_nacedoraRepository(Repository_get,Repository_create,Repository_update,Repository_delete):  
     def __init__(self):
         self.__model = Datos_sensores_nacedora

     def get_all(self) -> list[Datos_sensores_nacedora]:
        return db.session.query(self.__model).all()
        
     def get_by_id(self, id) -> Datos_sensores_nacedora:
         return db.session.query(self.__model).get(id)
     
     def create(self, entity: Datos_sensores_nacedora) -> Datos_sensores_nacedora:
         db.session.add(entity)
         db.session.commit()
         return entity
         
     def update(self, id, t: Datos_sensores_nacedora) -> Datos_sensores_nacedora:
         entity = self.get_by_id(id)
         if entity:
             entity.valor=t.valor
             entity.dia=t.dia
             db.session.add(entity)
             db.session.commit()
             return entity
         return None
         
     def delete(self, id)-> bool:
         datos_sensores_nacedora = self.get_by_id(id)
         if datos_sensores_nacedora:
             db.session.delete(datos_sensores_nacedora)
             db.session.commit()
             return True
         return False