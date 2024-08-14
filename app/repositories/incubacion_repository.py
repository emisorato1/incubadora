from app.models import Incubacion
from app import db
from .repository import Repository_get, Repository_create, Repository_update, Repository_delete


class IncubacionRepository(Repository_create,Repository_delete,Repository_update,Repository_get):
    def __init__(self):
        self.__model = Incubacion 
        
    def get_all(self) -> list[Incubacion]:
        return db.session.query(self.__model).all()

    def get_by_id(self, id) -> Incubacion:
        return db.session.query(self.__model).get(id)

    def create(self, entity: Incubacion) -> Incubacion:
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self, id, t: Incubacion) -> Incubacion:
        entity = self.get_by_id(id) 
        if entity: 
            entity.fecha_entrada=t.fecha_entrada
            entity.fecha_salida=t.fecha_salida
        
            db.session.add(entity)
            db.session.commit()
            return entity
        return None

    def delete(self, id) -> bool:
        Incubacion = self.get_by_id(id) 
        if Incubacion: 
            db.session.delete(Incubacion)
            db.session.commit()
            return Incubacion
        return None