from app.models import Detalles_incubacion
from app.repositories.detalles_incubacion_repository import Detalles_incubacionRepository


class Detalles_incubacionService:
    def __init__(self):
        self.repository = Detalles_incubacionRepository()

    def get_all(self) -> list[Detalles_incubacion]:
        detalles_incubaciones= self.repository.get_all()
        return list(detalles_incubaciones)
    
    def get_by_id(self, id)-> Detalles_incubacion:
        return self.repository.get_by_id(id)

    def create(self, entity: Detalles_incubacion)-> Detalles_incubacion:
        return self.repository.create(entity)

    def update(self, id, Detalles_incubacion) -> Detalles_incubacion:
        return self.repository.update(id, Detalles_incubacion)

    def delete(self, id)->bool:
        return self.repository.delete(id)