from app.models import Datos_sensores_nacedora
from app.repositories.datos_sensores_nacedora_repository import Datos_sensores_nacedoraRepository


class Datos_sensores_nacedoraService:
    def __init__(self):
        self.repository = Datos_sensores_nacedoraRepository()

    def get_all(self) -> list[Datos_sensores_nacedora]:
        datos_sensores_nacedoras= self.repository.get_all()
        return list(datos_sensores_nacedoras)
    
    def get_by_id(self, id)-> Datos_sensores_nacedora:
        return self.repository.get_by_id(id)

    def create(self, entity: Datos_sensores_nacedora)-> Datos_sensores_nacedora:
        return self.repository.create(entity)

    def update(self, id, Datos_sensores_nacedora) -> Datos_sensores_nacedora:
        return self.repository.update(id, Datos_sensores_nacedora)

    def delete(self, id)->bool:
        return self.repository.delete(id)