from app.models import Incubadora
from app import db
from .repository import Repository_get, Repository_create, Repository_update, Repository_delete


class IncubadoraRepository(Repository_create,Repository_delete,Repository_update,Repository_get):
    def __init__(self):
        self.__model = Incubadora 
        
    def get_all(self) -> list[Incubadora]:
        return db.session.query(self.__model).all()

    def get_by_id(self, id) -> Incubadora:
        return db.session.query(self.__model).get(id)

    def create(self, entity: Incubadora) -> Incubadora:
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self, id, t: Incubadora) -> Incubadora:
        entity = self.get_by_id(id) 
        if entity: 
            entity.modelo=t.modelo
                    
            db.session.add(entity)
            db.session.commit()
            return entity
        return None

    def delete(self, id) -> bool:
        incubadora = self.get_by_id(id) 
        if incubadora: 
            db.session.delete(incubadora)
            db.session.commit()
            return incubadora
        return None