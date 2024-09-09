from app.models import DatosSensorNacedora
from app import db
from .repository import Repository_get, Repository_create, Repository_update, Repository_delete


class DatosSensorNacedoraRepository(Repository_get,Repository_create,Repository_update,Repository_delete):  
     def __init__(self):
         self.__model = DatosSensorNacedora

     def get_all(self) -> list[DatosSensorNacedora]:
        return db.session.query(self.__model).all()
        
     def get_by_id(self, id) -> DatosSensorNacedora:
         return db.session.query(self.__model).get(id)
     
     def create(self, entity: DatosSensorNacedora) -> DatosSensorNacedora:
         db.session.add(entity)
         db.session.commit()
         return entity
         
     def update(self, id, t: DatosSensorNacedora) -> DatosSensorNacedora:
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