# Importamos las bibliotecas necesarias
import unittest
from flask import current_app
from app import create_app, db
from app.models.incubacion import Incubacion
from app.services.incubacion_services import IncubacionService
from datetime import datetime

incubacion_service = IncubacionService()

# Definimos la clase de prueba para el modelo User utilizando unittest
class IncubacionTestCase(unittest.TestCase):
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
    def test_incubacion(self):
        incubacion = self.__get_incubacion()        
        self.assertEqual(incubacion.fecha_entrada, self.fecha_entrada_prueba)
        self.assertEqual(incubacion.fecha_salida, self.fecha_salida_prueba)   
    
    # Prueba para verificar que el usuario se guarda correctamente en la base de datos
    def test_incubacion_save(self):
    
        incubacion = self.__get_incubacion()
        incubacion_service.create(incubacion)

        self.assertGreaterEqual(incubacion.id, 1)
        self.assertEqual(incubacion.fecha_entrada, self.fecha_entrada_prueba)
        self.assertEqual(incubacion.fecha_salida, self.fecha_salida_prueba)   
        
    # Prueba para verificar que el usuario se elimina correctamente de la base de datos
    def test_incubacion_delete(self):
        
        incubacion = self.__get_incubacion()
        incubacion_service.create(incubacion)

        # Borrar el usuario
        incubacion_service.delete(incubacion.id)
        self.assertIsNone(incubacion_service.get_by_id(1))
    
    # Prueba para verificar que se pueden obtener todos los usuarios
    def test_incubacion_all(self):
    
        incubacion = self.__get_incubacion()
        incubacion_service.create(incubacion)

        incubaciones = incubacion_service.get_all()
        self.assertGreaterEqual(len(incubaciones), 1)
    
    # Prueba para verificar que se puede encontrar un usuario por su ID
    def test_incubacion_find(self):
    
        incubacion = self.__get_incubacion()
        incubacion_service.create(incubacion)

        incubacion_find = incubacion_service.get_by_id(1)
        self.assertIsNotNone(incubacion_find)
        self.assertEqual(incubacion_find.id, incubacion.id)
        self.assertEqual(incubacion_find.fecha_entrada, incubacion.fecha_entrada)
    
    def __get_incubacion(self):
        incubacion = Incubacion()
        incubacion.fecha_entrada = self.fecha_entrada_prueba
        incubacion.fecha_salida = self.fecha_salida_prueba
        return incubacion
            
# Ejecutamos las pruebas si este script se ejecuta directamente
if __name__ == '__main__':
    unittest.main()
        