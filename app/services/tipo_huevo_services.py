from app.models import Tipo_huevo
from app.repositories.tipo_huevo_repository import Tipo_huevoRepository


class Tipo_huevoService:
    def __init__(self):
        self.repository = Tipo_huevoRepository()

    def get_all(self) -> list[Tipo_huevo]:
        tipo_huevos= self.repository.get_all()
        return list(tipo_huevos)
    
    def get_by_id(self, id)-> Tipo_huevo:
        return self.repository.get_by_id(id)

    def create(self, entity: Tipo_huevo)-> Tipo_huevo:
        return self.repository.create(entity)

    def update(self, id, Tipo_huevo) -> Tipo_huevo:
        return self.repository.update(id, Tipo_huevo)

    def delete(self, id)->bool:
        return self.repository.delete(id)