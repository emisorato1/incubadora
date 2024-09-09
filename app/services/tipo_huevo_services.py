from app.models import TipoHuevo
from app.repositories.tipo_huevo_repository import TipoHuevoRepository


class TipoHuevoService:
    def __init__(self):
        self.repository = TipoHuevoRepository()

    def get_all(self) -> list[TipoHuevo]:
        tipo_huevos= self.repository.get_all()
        return list(tipo_huevos)
    
    def get_by_id(self, id)-> TipoHuevo:
        return self.repository.get_by_id(id)

    def create(self, entity: TipoHuevo)-> TipoHuevo:
        return self.repository.create(entity)

    def update(self, id, Tipo_huevo) -> TipoHuevo:
        return self.repository.update(id, Tipo_huevo)

    def delete(self, id)->bool:
        return self.repository.delete(id)