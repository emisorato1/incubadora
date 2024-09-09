from app.models import DetallesNacimiento
from app import db
from .repository import Repository_get, Repository_create, Repository_update, Repository_delete


class DetallesNacimientoRepository(Repository_get,Repository_create,Repository_update,Repository_delete):  
     def __init__(self):
         self.__model = DetallesNacimiento

     def get_all(self) -> list[DetallesNacimiento]:
        return db.session.query(self.__model).all()
        
     def get_by_id(self, id) -> DetallesNacimiento:
         return db.session.query(self.__model).get(id)
     
     def create(self, entity: DetallesNacimiento) -> DetallesNacimiento:
         db.session.add(entity)
         db.session.commit()
         return entity
         
     def update(self, id, t: DetallesNacimiento) -> DetallesNacimiento:
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