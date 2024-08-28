from app.models import Detalles_nacimiento
from app import db
from .repository import Repository_get, Repository_create, Repository_update, Repository_delete


class Detalles_nacimientoRepository(Repository_get,Repository_create,Repository_update,Repository_delete):  
     def __init__(self):
         self.__model = Detalles_nacimiento

     def get_all(self) -> list[Detalles_nacimiento]:
        return db.session.query(self.__model).all()
        
     def get_by_id(self, id) -> Detalles_nacimiento:
         return db.session.query(self.__model).get(id)
     
     def create(self, entity: Detalles_nacimiento) -> Detalles_nacimiento:
         db.session.add(entity)
         db.session.commit()
         return entity
         
     def update(self, id, t: Detalles_nacimiento) -> Detalles_nacimiento:
         entity = self.get_by_id(id)
         if entity:
             entity.cant_huevos_inicial=t.cant_huevos_inicial
             entity.cant_huevos_final=t.cant_huevos_final
             db.session.add(entity)
             db.session.commit()
             return entity
         return None
         
     def delete(self, id)-> bool:
         detalles_nacimiento = self.get_by_id(id)
         if detalles_nacimiento:
             db.session.delete(detalles_nacimiento)
             db.session.commit()
             return True
         return False