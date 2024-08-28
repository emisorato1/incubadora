from app.models import Datos_sensores_incubadora
from app.repositories.datos_sensores_incubadora_repository import Datos_sensores_incubadoraRepository


class Datos_sensores_incubadoraService:
    def __init__(self):
        self.repository = Datos_sensores_incubadoraRepository()

    def get_all(self) -> list[Datos_sensores_incubadora]:
        datos_sensores_incubadoras= self.repository.get_all()
        return list(datos_sensores_incubadoras)
    
    def get_by_id(self, id)-> Datos_sensores_incubadora:
        return self.repository.get_by_id(id)

    def create(self, entity: Datos_sensores_incubadora)-> Datos_sensores_incubadora:
        return self.repository.create(entity)

    def update(self, id, Datos_sensores_incubadora) -> Datos_sensores_incubadora:
        return self.repository.update(id, Datos_sensores_incubadora)

    def delete(self, id)->bool:
        return self.repository.delete(id)