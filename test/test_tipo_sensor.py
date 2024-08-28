# Importamos las bibliotecas necesarias
import unittest
from flask import current_app
from app import create_app, db
from app.models.tipo_sensor import Tipo_sensor
from app.services.tipo_sensor_services import Tipo_sensorService

tipo_sensor_service = Tipo_sensorService()

# Definimos la clase de prueba para el modelo User utilizando unittest
class Tipo_sensorTestCase(unittest.TestCase):
    """
    Test User model
    Necesitamos aplicar principios como DRY (Don't Repeat Yourself) y KISS (Keep It Simple, Stupid).
    YAGNI (You Aren't Gonna Need It) y SOLID (Single Responsibility Principle).
    """

    # Configuramos el entorno de prueba
    def setUp(self):
        
        # Creamos la aplicación y el contexto de la aplicación para pruebas
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        # Creación de todas las tablas en la base de datos
        db.create_all()
        
        self.tipo_sensor_prueba = 'temperatura'
        
        
    # Limpiamos el entorno de prueba
    def tearDown(self):
        # Eliminamos la sesión y todas las tablas de la base de datos
        db.session.remove()
        db.drop_all()
        # Sacamos el contexto de la aplicación
        self.app_context.pop()

    # Prueba para verificar que la aplicación se crea correctamente
    def test_app(self):
        self.assertIsNotNone(current_app)
    
    # Prueba para verificar que los atributos del usuario se establecen correctamente
    def test_tipo_sensor(self):
        tipo_sensor = self.__get_tipo_sensor()        
        self.assertEqual(tipo_sensor.tipo_sensor, self.tipo_sensor_prueba)
    
    # Prueba para verificar que el usuario se guarda correctamente en la base de datos
    def test_tipo_sensor_save(self):
        tipo_sensor = self.__get_tipo_sensor()
        tipo_sensor_service.create(tipo_sensor)

        self.assertGreaterEqual(tipo_sensor.id, 1)
        self.assertEqual(tipo_sensor.tipo_sensor, self.tipo_sensor_prueba)
        
    # Prueba para verificar que el usuario se elimina correctamente de la base de datos
    def test_tipo_sensor_delete(self):       
        tipo_sensor = self.__get_tipo_sensor()
        tipo_sensor_service.create(tipo_sensor)

        # Borrar el usuario
        tipo_sensor_service.delete(tipo_sensor.id)
        self.assertIsNone(tipo_sensor_service.get_by_id(1))
    
    # Prueba para verificar que se pueden obtener todos los usuarios
    def test_tipo_sensor_all(self):
    
        tipo_sensor = self.__get_tipo_sensor()
        tipo_sensor_service.create(tipo_sensor)

        tipo_sensors = tipo_sensor_service.get_all()
        self.assertGreaterEqual(len(tipo_sensors), 1)
    
    # Prueba para verificar que se puede encontrar un usuario por su ID
    def test_tipo_sensor_find(self):
    
        tipo_sensor = self.__get_tipo_sensor()
        tipo_sensor_service.create(tipo_sensor)

        tipo_sensor_find = tipo_sensor_service.get_by_id(1)
        self.assertIsNotNone(tipo_sensor_find)
        self.assertEqual(tipo_sensor_find.id, tipo_sensor.id)
        self.assertEqual(tipo_sensor_find.tipo_sensor, tipo_sensor.tipo_sensor)
    
    def __get_tipo_sensor(self):
        tipo_sensor = Tipo_sensor()
        tipo_sensor.tipo_sensor = self.tipo_sensor_prueba
        return tipo_sensor
            
# Ejecutamos las pruebas si este script se ejecuta directamente
if __name__ == '__main__':
    unittest.main()