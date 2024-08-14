from app.models import Nacimiento
from app import db
from .repository import Repository_get, Repository_create, Repository_update, Repository_delete


class NacimientoRepository(Repository_create,Repository_delete,Repository_update,Repository_get):
    def __init__(self):
        self.__model = Nacimiento 
        
    def get_all(self) -> list[Nacimiento]:
        return db.session.query(self.__model).all()

    def get_by_id(self, id) -> Nacimiento:
        return db.session.query(self.__model).get(id)

    def create(self, entity: Nacimiento) -> Nacimiento:
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self, id, t: Nacimiento) -> Nacimiento:
        entity = self.get_by_id(id) 
        if entity: 
            entity.fecha_entrada=t.fecha_entrada
            entity.fecha_salida=t.fecha_salida
        
            db.session.add(entity)
            db.session.commit()
            return entity
        return None

    def delete(self, id) -> bool:
        Nacimiento = self.get_by_id(id) 
        if Nacimiento: 
            db.session.delete(Nacimiento)
            db.session.commit()
            return Nacimiento
        return None