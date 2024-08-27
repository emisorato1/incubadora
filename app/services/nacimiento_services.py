from app.models import Nacimiento
from app.repositories.nacimiento_repository import NacimientoRepository


class NacimientoService:
    def __init__(self):
        self.repository = NacimientoRepository()

    def get_all(self) -> list[Nacimiento]:
        incubaciones= self.repository.get_all()
        return list(incubaciones)
    
    def get_by_id(self, id)-> Nacimiento:
        return self.repository.get_by_id(id)

    def create(self, entity: Nacimiento)-> Nacimiento:
        return self.repository.create(entity)

    def update(self, id, Nacimiento) -> Nacimiento:
        return self.repository.update(id, Nacimiento)

    def delete(self, id)->bool:
        return self.repository.delete(id)