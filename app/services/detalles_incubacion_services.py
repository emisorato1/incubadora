from app.models import DetallesIncubacion
from app.repositories.detalles_incubacion_repository import DetallesIncubacionRepository


class DetallesIncubacionService:
    def __init__(self):
        self.repository = DetallesIncubacionRepository()

    def get_all(self) -> list[DetallesIncubacion]:
        detalles_incubaciones= self.repository.get_all()
        return list(detalles_incubaciones)
    
    def get_by_id(self, id)-> DetallesIncubacion:
        return self.repository.get_by_id(id)

    def create(self, entity: DetallesIncubacion)-> DetallesIncubacion:
        return self.repository.create(entity)

    def update(self, id, Detalles_incubacion) -> DetallesIncubacion:
        return self.repository.update(id, Detalles_incubacion)

    def delete(self, id)->bool:
        return self.repository.delete(id)