from app.models import DetallesIncubacion
from app import db
from .repository import Repository_get, Repository_create, Repository_update, Repository_delete


class DetallesIncubacionRepository(Repository_get,Repository_create,Repository_update,Repository_delete):  
     def __init__(self):
         self.__model = DetallesIncubacion

     def get_all(self) -> list[DetallesIncubacion]:
        return db.session.query(self.__model).all()
        
     def get_by_id(self, id) -> DetallesIncubacion:
         return db.session.query(self.__model).get(id)
     
     def create(self, entity: DetallesIncubacion) -> DetallesIncubacion:
         db.session.add(entity)
         db.session.commit()
         return entity
         
     def update(self, id, t: DetallesIncubacion) -> DetallesIncubacion:
         entity = self.get_by_id(id)
         if entity:
             entity.cant_huevos_inicial=t.cant_huevos_inicial
             entity.cant_huevos_final=t.cant_huevos_final
             db.session.add(entity)
             db.session.commit()
             return entity
         return None
         
     def delete(self, id)-> bool:
         detalles_incubacion = self.get_by_id(id)
         if detalles_incubacion:
             db.session.delete(detalles_incubacion)
             db.session.commit()
             return True
         return False