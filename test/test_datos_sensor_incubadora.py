# Importamos las bibliotecas necesarias
import unittest
from flask import current_app
from app import create_app, db
from app.models import DatosSensorIncubadora
from app.services import DatosSensorIncubadoraService
from datetime import datetime

datos_sensor_incubadora_service = DatosSensorIncubadoraService()

# Definimos la clase de prueba para el modelo User utilizando unittest
class DatosSensorIncubadoraTestCase(unittest.TestCase):
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
        
        self.valor_prueba = 30
        self.dia_prueba = datetime.strptime('12/05/2024', '%d/%m/%Y')
     
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
    def test_datos_sensor_incubadora(self):
        datos_sensor_incubadora = self.__get_datos_sensor_incubadora()        
        self.assertEqual(datos_sensor_incubadora.valor, self.valor_prueba)
        self.assertEqual(datos_sensor_incubadora.dia, self.dia_prueba)
    
    # Prueba para verificar que el usuario se guarda correctamente en la base de datos
    def test_datos_sensor_incubadora_save(self):
        datos_sensor_incubadora = self.__get_datos_sensor_incubadora()
        datos_sensor_incubadora_service.create(datos_sensor_incubadora)

        self.assertGreaterEqual(datos_sensor_incubadora.id, 1)
        self.assertEqual(datos_sensor_incubadora.valor, self.valor_prueba)
        self.assertEqual(datos_sensor_incubadora.dia, self.dia_prueba)
        
    # Prueba para verificar que el usuario se elimina correctamente de la base de datos
    def test_datos_sensor_incubadora_delete(self):       
        datos_sensor_incubadora = self.__get_datos_sensor_incubadora()
        datos_sensor_incubadora_service.create(datos_sensor_incubadora)

        # Borrar el usuario
        datos_sensor_incubadora_service.delete(datos_sensor_incubadora.id)
        self.assertIsNone(datos_sensor_incubadora_service.get_by_id(1))
    
    # Prueba para verificar que se pueden obtener todos los usuarios
    def test_datos_sensor_incubadora_all(self):
    
        datos_sensor_incubadora = self.__get_datos_sensor_incubadora()
        datos_sensor_incubadora_service.create(datos_sensor_incubadora)

        datos_sensor_incubadoras = datos_sensor_incubadora_service.get_all()
        self.assertGreaterEqual(len(datos_sensor_incubadoras), 1)
    
    # Prueba para verificar que se puede encontrar un usuario por su ID
    def test_datos_sensor_incubadora_find(self):
    
        datos_sensor_incubadora = self.__get_datos_sensor_incubadora()
        datos_sensor_incubadora_service.create(datos_sensor_incubadora)

        datos_sensor_incubadora_find = datos_sensor_incubadora_service.get_by_id(1)
        self.assertIsNotNone(datos_sensor_incubadora_find)
        self.assertEqual(datos_sensor_incubadora_find.id, datos_sensor_incubadora.id)
        self.assertEqual(datos_sensor_incubadora.dia, self.dia_prueba)
    
    def __get_datos_sensor_incubadora(self):
        datos_sensor_incubadora = DatosSensorIncubadora()
        datos_sensor_incubadora.valor = self.valor_prueba
        datos_sensor_incubadora.dia = self.dia_prueba
        return datos_sensor_incubadora
            
# Ejecutamos las pruebas si este script se ejecuta directamente
if __name__ == '__main__':
    unittest.main()