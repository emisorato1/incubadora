from app.models import Tipo_sensor
from app.repositories.tipo_sensor_repository import Tipo_sensorRepository


class Tipo_sensorService:
    def __init__(self):
        self.repository = Tipo_sensorRepository()

    def get_all(self) -> list[Tipo_sensor]:
        tipo_sensores= self.repository.get_all()
        return list(tipo_sensores)
    
    def get_by_id(self, id)-> Tipo_sensor:
        return self.repository.get_by_id(id)

    def create(self, entity: Tipo_sensor)-> Tipo_sensor:
        return self.repository.create(entity)

    def update(self, id, Tipo_sensor) -> Tipo_sensor:
        return self.repository.update(id, Tipo_sensor)

    def delete(self, id)->bool:
        return self.repository.delete(id)