# Importamos las bibliotecas necesarias
import unittest
from flask import current_app
from app import create_app, db
from app.models.nacedora import Nacedora
from app.services.nacedora_services import NacedoraService

nacedora_services = NacedoraService()

# Definimos la clase de prueba para el modelo User utilizando unittest
class IncubadoraTestCase(unittest.TestCase):
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
        
        self.modelo_prueba = 'nuevo'
        
        
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
    def test_nacedora(self):
        nacedora = self.__get_nacedora()        
        self.assertEqual(nacedora.modelo, self.modelo_prueba)
    
    # Prueba para verificar que el usuario se guarda correctamente en la base de datos
    def test_nacedora_save(self):
    
        nacedora = self.__get_nacedora()
        nacedora_services.create(nacedora)

        self.assertGreaterEqual(nacedora.id, 1)
        self.assertEqual(nacedora.modelo, self.modelo_prueba)
        
    # Prueba para verificar que el usuario se elimina correctamente de la base de datos
    def test_nacedora_delete(self):
        
        nacedora = self.__get_nacedora()
        nacedora_services.create(nacedora)

        # Borrar el usuario
        nacedora_services.delete(nacedora.id)
        self.assertIsNone(nacedora_services.get_by_id(1))
    
    # Prueba para verificar que se pueden obtener todos los usuarios0
    def test_nacedora_all(self):
    
        nacedora = self.__get_nacedora()
        nacedora_services.create(nacedora)

        nacedoras = nacedora_services.get_all()
        self.assertGreaterEqual(len(nacedoras), 1)
    
    # Prueba para verificar que se puede encontrar un usuario por su ID
    def test_nacedora_find(self):
    
        nacedora = self.__get_nacedora()
        nacedora_services.create(nacedora)

        nacedora_find = nacedora_services.get_by_id(1)
        self.assertIsNotNone(nacedora_find)
        self.assertEqual(nacedora_find.id, nacedora.id)
        self.assertEqual(nacedora_find.modelo, nacedora.modelo)
    
    def __get_nacedora(self):
        nacedora = Nacedora()
        nacedora.modelo = self.modelo_prueba
        return nacedora
            
# Ejecutamos las pruebas si este script se ejecuta directamente
if __name__ == '__main__':
    unittest.main()