# Importamos las bibliotecas necesarias
import unittest
from flask import current_app
from app import create_app, db
from app.models.incubadora import Incubadora
from app.services.incubadora_sevices import IncubadoraService

incubadora_service = IncubadoraService()

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
    def test_incubadora(self):
        incubadora = self.__get_incubadora()        
        self.assertEqual(incubadora.modelo, self.modelo_prueba)
    
    # Prueba para verificar que el usuario se guarda correctamente en la base de datos
    def test_incubadora_save(self):
    
        incubadora = self.__get_incubadora()
        incubadora_service.create(incubadora)

        self.assertGreaterEqual(incubadora.id, 1)
        self.assertEqual(incubadora.modelo, self.modelo_prueba)
        
    # Prueba para verificar que el usuario se elimina correctamente de la base de datos
    def test_incubadora_delete(self):
        
        incubadora = self.__get_incubadora()
        incubadora_service.create(incubadora)

        # Borrar el usuario
        incubadora_service.delete(incubadora.id)
        self.assertIsNone(incubadora_service.get_by_id(1))
    
    # Prueba para verificar que se pueden obtener todos los usuarios
    def test_incubadora_all(self):
    
        incubadora = self.__get_incubadora()
        incubadora_service.create(incubadora)

        incubadoras = incubadora_service.get_all()
        self.assertGreaterEqual(len(incubadoras), 1)
    
    # Prueba para verificar que se puede encontrar un usuario por su ID
    def test_incubadora_find(self):
    
        incubadora = self.__get_incubadora()
        incubadora_service.create(incubadora)

        incubadora_find = incubadora_service.get_by_id(1)
        self.assertIsNotNone(incubadora_find)
        self.assertEqual(incubadora_find.id, incubadora.id)
        self.assertEqual(incubadora_find.modelo, incubadora.modelo)
    
    def __get_incubadora(self):
        incubadora = Incubadora()
        incubadora.modelo = self.modelo_prueba
        return incubadora
            
# Ejecutamos las pruebas si este script se ejecuta directamente
if __name__ == '__main__':
    unittest.main()