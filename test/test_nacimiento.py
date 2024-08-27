# Importamos las bibliotecas necesarias
import unittest
from flask import current_app
from app import create_app, db
from app.models.nacimiento import Nacimiento
from app.services.nacimiento_services import NacimientoService
from datetime import datetime

nacimiento_service = NacimientoService()

# Definimos la clase de prueba para el modelo User utilizando unittest
class NacimientoTestCase(unittest.TestCase):
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
        
        self.fecha_entrada_prueba = datetime.strptime('10/05/2024', '%d/%m/%Y')
        self.fecha_salida_prueba = datetime.strptime('15/05/2024', '%d/%m/%Y')
        
        
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
    def test_nacimiento(self):
        nacimiento = self.__get_nacimiento()        
        self.assertEqual(nacimiento.fecha_entrada, self.fecha_entrada_prueba)
        self.assertEqual(nacimiento.fecha_salida, self.fecha_salida_prueba)   
    
    # Prueba para verificar que el usuario se guarda correctamente en la base de datos
    def test_nacimiento_save(self):
        nacimiento = self.__get_nacimiento()
        nacimiento_service.create(nacimiento)

        self.assertGreaterEqual(nacimiento.id, 1)
        self.assertEqual(nacimiento.fecha_entrada, self.fecha_entrada_prueba)
        self.assertEqual(nacimiento.fecha_salida, self.fecha_salida_prueba)   
        
    # Prueba para verificar que el usuario se elimina correctamente de la base de datos
    def test_nacimiento_delete(self):       
        nacimiento = self.__get_nacimiento()
        nacimiento_service.create(nacimiento)

        # Borrar el usuario
        nacimiento_service.delete(nacimiento.id)
        self.assertIsNone(nacimiento_service.get_by_id(1))
    
    # Prueba para verificar que se pueden obtener todos los usuarios
    def test_nacimiento_all(self):
    
        nacimiento = self.__get_nacimiento()
        nacimiento_service.create(nacimiento)

        nacimientos = nacimiento_service.get_all()
        self.assertGreaterEqual(len(nacimientos), 1)
    
    # Prueba para verificar que se puede encontrar un usuario por su ID
    def test_nacimiento_find(self):
    
        nacimiento = self.__get_nacimiento()
        nacimiento_service.create(nacimiento)

        incubacion_find = nacimiento_service.get_by_id(1)
        self.assertIsNotNone(incubacion_find)
        self.assertEqual(incubacion_find.id, nacimiento.id)
        self.assertEqual(incubacion_find.fecha_entrada, nacimiento.fecha_entrada)
    
    def __get_nacimiento(self):
        nacimiento = Nacimiento()
        nacimiento.fecha_entrada = self.fecha_entrada_prueba
        nacimiento.fecha_salida = self.fecha_salida_prueba
        return nacimiento
            
# Ejecutamos las pruebas si este script se ejecuta directamente
if __name__ == '__main__':
    unittest.main()
        