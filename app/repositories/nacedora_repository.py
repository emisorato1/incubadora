from app.models import Nacedora
from app import db
from .repository import Repository_get, Repository_create, Repository_update, Repository_delete


class NacedoraRepository(Repository_create,Repository_delete,Repository_update,Repository_get):
    def __init__(self):
        self.__model = Nacedora 
        
    def get_all(self) -> list[Nacedora]:
        return db.session.query(self.__model).all()

    def get_by_id(self, id) -> Nacedora:
        return db.session.query(self.__model).get(id)

    def create(self, entity: Nacedora) -> Nacedora:
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self, id, t: Nacedora) -> Nacedora:
        entity = self.get_by_id(id) 
        if entity: 
            entity.modelo=t.modelo
                    
            db.session.add(entity)
            db.session.commit()
            return entity
        return None

    def delete(self, id) -> bool:
        nacedora = self.get_by_id(id) 
        if nacedora: 
            db.session.delete(nacedora)
            db.session.commit()
            return nacedora
        return None