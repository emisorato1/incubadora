from app.models import Nacedora
from app.repositories.nacedora_repository import NacedoraRepository


class NacedoraService:
    def __init__(self):
        self.repository = NacedoraRepository()

    def get_all(self) -> list[Nacedora]:
        nacedora= self.repository.get_all()
        return list(nacedora)
    
    def get_by_id(self, id)-> Nacedora:
        return self.repository.get_by_id(id)

    def create(self, entity: Nacedora)-> Nacedora:
        return self.repository.create(entity)

    def update(self, id, Nacedora) -> Nacedora:
        return self.repository.update(id, Nacedora)

    def delete(self, id)->bool:
        return self.repository.delete(id)