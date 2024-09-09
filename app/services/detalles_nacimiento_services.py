from app.models import DetallesNacimiento
from app.repositories.detalles_nacimiento_repository import DetallesNacimientoRepository


class DetallesNacimientoService:
    def __init__(self):
        self.repository = DetallesNacimientoRepository()

    def get_all(self) -> list[DetallesNacimiento]:
        detalles_nacimientos= self.repository.get_all()
        return list(detalles_nacimientos)
    
    def get_by_id(self, id)-> DetallesNacimiento:
        return self.repository.get_by_id(id)

    def create(self, entity: DetallesNacimiento)-> DetallesNacimiento:
        return self.repository.create(entity)

    def update(self, id, Detalles_nacimiento) -> DetallesNacimiento:
        return self.repository.update(id, Detalles_nacimiento)

    def delete(self, id)->bool:
        return self.repository.delete(id)