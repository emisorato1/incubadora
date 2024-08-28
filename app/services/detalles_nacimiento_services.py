from app.models import Detalles_nacimiento
from app.repositories.detalles_nacimiento_repository import Detalles_nacimientoRepository


class Detalles_nacimientoService:
    def __init__(self):
        self.repository = Detalles_nacimientoRepository()

    def get_all(self) -> list[Detalles_nacimiento]:
        detalles_nacimientos= self.repository.get_all()
        return list(detalles_nacimientos)
    
    def get_by_id(self, id)-> Detalles_nacimiento:
        return self.repository.get_by_id(id)

    def create(self, entity: Detalles_nacimiento)-> Detalles_nacimiento:
        return self.repository.create(entity)

    def update(self, id, Detalles_nacimiento) -> Detalles_nacimiento:
        return self.repository.update(id, Detalles_nacimiento)

    def delete(self, id)->bool:
        return self.repository.delete(id)