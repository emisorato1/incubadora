from app.models import Incubadora
from app.repositories.incubadora_repository import IncubadoraRepository


class IncubadoraService:
    def __init__(self):
        self.repository = IncubadoraRepository()

    def get_all(self) -> list[Incubadora]:
        incubadora= self.repository.get_all()
        return list(incubadora)
    
    def get_by_id(self, id)-> Incubadora:
        return self.repository.get_by_id(id)

    def create(self, entity: Incubadora)-> Incubadora:
        return self.repository.create(entity)

    def update(self, id, Incubadora) -> Incubadora:
        return self.repository.update(id, Incubadora)

    def delete(self, id)->bool:
        return self.repository.delete(id)