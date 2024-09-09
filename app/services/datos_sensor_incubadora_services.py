from app.models import DatosSensorIncubadora
from app.repositories.datos_sensor_incubadora_repository import DatosSensorIncubadoraRepository


class DatosSensorIncubadoraService:
    def __init__(self):
        self.repository = DatosSensorIncubadoraRepository()

    def get_all(self) -> list[DatosSensorIncubadora]:
        datos_sensor_incubadoras= self.repository.get_all()
        return list(datos_sensor_incubadoras)
    
    def get_by_id(self, id)-> DatosSensorIncubadora:
        return self.repository.get_by_id(id)

    def create(self, entity: DatosSensorIncubadora)-> DatosSensorIncubadora:
        return self.repository.create(entity)

    def update(self, id, datos_sensor_incubadora) -> DatosSensorIncubadora:
        return self.repository.update(id, datos_sensor_incubadora)

    def delete(self, id)->bool:
        return self.repository.delete(id)