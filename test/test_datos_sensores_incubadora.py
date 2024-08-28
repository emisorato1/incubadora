# Importamos las bibliotecas necesarias
import unittest
from flask import current_app
from app import create_app, db
from app.models.datos_sensores_incubadora import Datos_sensores_incubadora
from app.services.datos_sensores_incubadora_services import Datos_sensores_incubadoraService
from datetime import datetime

datos_sensores_incubadora_service = Datos_sensores_incubadoraService()

# Definimos la clase de prueba para el modelo User utilizando unittest
class Datos_sensores_incubadoraTestCase(unittest.TestCase):
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
    def test_datos_sensores_incubadora(self):
        datos_sensores_incubadora = self.__get_datos_sensores_incubadora()        
        self.assertEqual(datos_sensores_incubadora.valor, self.valor_prueba)
        self.assertEqual(datos_sensores_incubadora.dia, self.dia_prueba)
    
    # Prueba para verificar que el usuario se guarda correctamente en la base de datos
    def test_datos_sensores_incubadora_save(self):
        datos_sensores_incubadora = self.__get_datos_sensores_incubadora()
        datos_sensores_incubadora_service.create(datos_sensores_incubadora)

        self.assertGreaterEqual(datos_sensores_incubadora.id, 1)
        self.assertEqual(datos_sensores_incubadora.valor, self.valor_prueba)
        self.assertEqual(datos_sensores_incubadora.dia, self.dia_prueba)
        
    # Prueba para verificar que el usuario se elimina correctamente de la base de datos
    def test_datos_sensores_incubadora_delete(self):       
        datos_sensores_incubadora = self.__get_datos_sensores_incubadora()
        datos_sensores_incubadora_service.create(datos_sensores_incubadora)

        # Borrar el usuario
        datos_sensores_incubadora_service.delete(datos_sensores_incubadora.id)
        self.assertIsNone(datos_sensores_incubadora_service.get_by_id(1))
    
    # Prueba para verificar que se pueden obtener todos los usuarios
    def test_datos_sensores_incubadora_all(self):
    
        datos_sensores_incubadora = self.__get_datos_sensores_incubadora()
        datos_sensores_incubadora_service.create(datos_sensores_incubadora)

        datos_sensores_incubadoras = datos_sensores_incubadora_service.get_all()
        self.assertGreaterEqual(len(datos_sensores_incubadoras), 1)
    
    # Prueba para verificar que se puede encontrar un usuario por su ID
    def test_datos_sensores_incubadora_find(self):
    
        datos_sensores_incubadora = self.__get_datos_sensores_incubadora()
        datos_sensores_incubadora_service.create(datos_sensores_incubadora)

        datos_sensores_incubadora_find = datos_sensores_incubadora_service.get_by_id(1)
        self.assertIsNotNone(datos_sensores_incubadora_find)
        self.assertEqual(datos_sensores_incubadora_find.id, datos_sensores_incubadora.id)
        self.assertEqual(datos_sensores_incubadora.dia, self.dia_prueba)
    
    def __get_datos_sensores_incubadora(self):
        datos_sensores_incubadora = Datos_sensores_incubadora()
        datos_sensores_incubadora.valor = self.valor_prueba
        datos_sensores_incubadora.dia = self.dia_prueba
        return datos_sensores_incubadora
            
# Ejecutamos las pruebas si este script se ejecuta directamente
if __name__ == '__main__':
    unittest.main()