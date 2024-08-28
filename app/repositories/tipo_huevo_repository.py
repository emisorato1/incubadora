from app.models import Tipo_huevo
from app import db
from .repository import Repository_get, Repository_create, Repository_update, Repository_delete


class Tipo_huevoRepository(Repository_get,Repository_create,Repository_update,Repository_delete):  
     def __init__(self):
         self.__model = Tipo_huevo

     def get_all(self) -> list[Tipo_huevo]:
        return db.session.query(self.__model).all()
        
     def get_by_id(self, id) -> Tipo_huevo:
         return db.session.query(self.__model).get(id)
     
     def create(self, entity: Tipo_huevo) -> Tipo_huevo:
         db.session.add(entity)
         db.session.commit()
         return entity
         
     def update(self, id, t: Tipo_huevo) -> Tipo_huevo:
         entity = self.get_by_id(id)
         if entity:
             entity.tipo_huevo=t.tipo_huevo
             db.session.add(entity)
             db.session.commit()
             return entity
         return None
         
     def delete(self, id)-> bool:
         Tipo_huevo = self.get_by_id(id)
         if Tipo_huevo:
             db.session.delete(Tipo_huevo)
             db.session.commit()
             return True
         return False