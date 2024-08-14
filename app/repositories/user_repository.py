from app.models import User
from app import db
from .repository import Repository_get, Repository_create, Repository_update, Repository_delete


class UserRepository(Repository_get,Repository_create,Repository_update,Repository_delete):  
     def __init__(self):
         self.__model = User

     def get_all(self) -> list[User]:
        try:
            return db.session.query(self.__model).all()
        except Exception as e:
            print(f"error al buscar los usuarios {e}")
            return []
        
     def get_by_id(self, id) -> User:
         return db.session.query(self.__model).get(id)
     
     
     def create(self, entity: User) -> User:
         db.session.add(entity)
         db.session.commit()
         return entity
     
     
     def update(self, id, t: User) -> User:
         entity = self.get_by_id(id)
         if entity:
             entity.password=t.password
             entity.role=t.role
             entity.user_name=t.user_name
             db.session.add(entity)
             db.session.commit()
             return entity
         return None
     
     
     def delete(self, id)-> bool:
         user = self.get_by_id(id)
         if user:
             db.session.delete(user)
             db.session.commit()
             return True
         return False