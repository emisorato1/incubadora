from app.models import TipoSensor
from app.repositories.tipo_sensor_repository import TipoSensorRepository


class TipoSensorService:
    def __init__(self):
        self.repository = TipoSensorRepository()

    def get_all(self) -> list[TipoSensor]:
        tipo_sensores= self.repository.get_all()
        return list(tipo_sensores)
    
    def get_by_id(self, id)-> TipoSensor:
        return self.repository.get_by_id(id)

    def create(self, entity: TipoSensor)-> TipoSensor:
        return self.repository.create(entity)

    def update(self, id, Tipo_sensor) -> TipoSensor:
        return self.repository.update(id, Tipo_sensor)

    def delete(self, id)->bool:
        return self.repository.delete(id)