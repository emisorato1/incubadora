# Importamos las bibliotecas necesarias
import unittest
from flask import current_app
from app import create_app, db
from app.models.tipo_huevo import Tipo_huevo
from app.services.tipo_huevo_services import Tipo_huevoService

tipo_huevo_service = Tipo_huevoService()

# Definimos la clase de prueba para el modelo User utilizando unittest
class Tipo_huevoTestCase(unittest.TestCase):
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
        
        self.tipo_huevo_prueba = 'temperatura'
        
        
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
    def test_tipo_huevo(self):
        tipo_huevo = self.__get_tipo_huevo()        
        self.assertEqual(tipo_huevo.tipo_huevo, self.tipo_huevo_prueba)
    
    # Prueba para verificar que el usuario se guarda correctamente en la base de datos
    def test_tipo_huevo_save(self):
        tipo_huevo = self.__get_tipo_huevo()
        tipo_huevo_service.create(tipo_huevo)

        self.assertGreaterEqual(tipo_huevo.id, 1)
        self.assertEqual(tipo_huevo.tipo_huevo, self.tipo_huevo_prueba)
        
    # Prueba para verificar que el usuario se elimina correctamente de la base de datos
    def test_tipo_huevo_delete(self):       
        tipo_huevo = self.__get_tipo_huevo()
        tipo_huevo_service.create(tipo_huevo)

        # Borrar el usuario
        tipo_huevo_service.delete(tipo_huevo.id)
        self.assertIsNone(tipo_huevo_service.get_by_id(1))
    
    # Prueba para verificar que se pueden obtener todos los usuarios
    def test_tipo_huevo_all(self):
    
        tipo_huevo = self.__get_tipo_huevo()
        tipo_huevo_service.create(tipo_huevo)

        tipo_huevos = tipo_huevo_service.get_all()
        self.assertGreaterEqual(len(tipo_huevos), 1)
    
    # Prueba para verificar que se puede encontrar un usuario por su ID
    def test_tipo_huevo_find(self):
    
        tipo_huevo = self.__get_tipo_huevo()
        tipo_huevo_service.create(tipo_huevo)

        tipo_huevo_find = tipo_huevo_service.get_by_id(1)
        self.assertIsNotNone(tipo_huevo_find)
        self.assertEqual(tipo_huevo_find.id, tipo_huevo.id)
        self.assertEqual(tipo_huevo_find.tipo_huevo, tipo_huevo.tipo_huevo)
    
    def __get_tipo_huevo(self):
        tipo_huevo = Tipo_huevo()
        tipo_huevo.tipo_huevo = self.tipo_huevo_prueba
        return tipo_huevo
            
# Ejecutamos las pruebas si este script se ejecuta directamente
if __name__ == '__main__':
    unittest.main()