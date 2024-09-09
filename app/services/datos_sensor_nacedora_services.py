from app.models import DatosSensorNacedora
from app.repositories.datos_sensor_nacedora_repository import DatosSensorNacedoraRepository


class DatosSensorNacedoraService:
    def __init__(self):
        self.repository = DatosSensorNacedoraRepository()

    def get_all(self) -> list[DatosSensorNacedora]:
        datos_sensor_nacedoras= self.repository.get_all()
        return list(datos_sensor_nacedoras)
    
    def get_by_id(self, id)-> DatosSensorNacedora:
        return self.repository.get_by_id(id)

    def create(self, entity: DatosSensorNacedora)-> DatosSensorNacedora:
        return self.repository.create(entity)

    def update(self, id, datos_sensor_nacedora) -> DatosSensorNacedora:
        return self.repository.update(id, datos_sensor_nacedora)

    def delete(self, id)->bool:
        return self.repository.delete(id)