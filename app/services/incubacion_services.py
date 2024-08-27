from app.models import Incubacion
from app.repositories.incubacion_repository import IncubacionRepository


class IncubacionService:
    def __init__(self):
        self.repository = IncubacionRepository()

    def get_all(self) -> list[Incubacion]:
        incubaciones= self.repository.get_all()
        return list(incubaciones)
    
    def get_by_id(self, id)-> Incubacion:
        return self.repository.get_by_id(id)

    def create(self, entity: Incubacion)-> Incubacion:
        return self.repository.create(entity)

    def update(self, id, Incubacion) -> Incubacion:
        return self.repository.update(id, Incubacion)

    def delete(self, id)->bool:
        return self.repository.delete(id)