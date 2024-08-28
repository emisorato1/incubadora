from app.models import Datos_sensores_incubadora
from app import db
from .repository import Repository_get, Repository_create, Repository_update, Repository_delete


class Datos_sensores_incubadoraRepository(Repository_get,Repository_create,Repository_update,Repository_delete):  
     def __init__(self):
         self.__model = Datos_sensores_incubadora

     def get_all(self) -> list[Datos_sensores_incubadora]:
        return db.session.query(self.__model).all()
        
     def get_by_id(self, id) -> Datos_sensores_incubadora:
         return db.session.query(self.__model).get(id)
     
     def create(self, entity: Datos_sensores_incubadora) -> Datos_sensores_incubadora:
         db.session.add(entity)
         db.session.commit()
         return entity
         
     def update(self, id, t: Datos_sensores_incubadora) -> Datos_sensores_incubadora:
         entity = self.get_by_id(id)
         if entity:
             entity.valor=t.valor
             entity.dia=t.dia
             db.session.add(entity)
             db.session.commit()
             return entity
         return None
         
     def delete(self, id)-> bool:
         datos_sensores_incubadora = self.get_by_id(id)
         if datos_sensores_incubadora:
             db.session.delete(datos_sensores_incubadora)
             db.session.commit()
             return True
         return False