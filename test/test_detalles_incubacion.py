# Importamos las bibliotecas necesarias
import unittest
from flask import current_app
from app import create_app, db
from app.models.detalles_incubacion import DetallesIncubacion
from app.services.detalles_incubacion_services import DetallesIncubacionService

detalles_incubacion_service = DetallesIncubacionService()

# Definimos la clase de prueba para el modelo User utilizando unittest
class Detalles_incubacionTestCase(unittest.TestCase):
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
        
        self.cant_huevos_inicial_prueba = 40
        self.cant_huevos_final_prueba = 35

        
        
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
    def test_detalles_incubacion(self):
        detalles_incubacion = self.__get_detalles_incubacion()        
        self.assertEqual(detalles_incubacion.cant_huevos_inicial, self.cant_huevos_inicial_prueba)
        self.assertEqual(detalles_incubacion.cant_huevos_final, self.cant_huevos_final_prueba)
    
    # Prueba para verificar que el usuario se guarda correctamente en la base de datos
    def test_detalles_incubacion_save(self):
        detalles_incubacion = self.__get_detalles_incubacion()
        detalles_incubacion_service.create(detalles_incubacion)

        self.assertGreaterEqual(detalles_incubacion.id, 1)
        self.assertEqual(detalles_incubacion.cant_huevos_inicial, self.cant_huevos_inicial_prueba)
        self.assertEqual(detalles_incubacion.cant_huevos_final, self.cant_huevos_final_prueba)
        
    # Prueba para verificar que el usuario se elimina correctamente de la base de datos
    def test_detalles_incubacion_delete(self):       
        detalles_incubacion = self.__get_detalles_incubacion()
        detalles_incubacion_service.create(detalles_incubacion)

        # Borrar el usuario
        detalles_incubacion_service.delete(detalles_incubacion.id)
        self.assertIsNone(detalles_incubacion_service.get_by_id(1))
    
    # Prueba para verificar que se pueden obtener todos los usuarios
    def test_detalles_incubacion_all(self):
    
        detalles_incubacion = self.__get_detalles_incubacion()
        detalles_incubacion_service.create(detalles_incubacion)

        detalles_incubacions = detalles_incubacion_service.get_all()
        self.assertGreaterEqual(len(detalles_incubacions), 1)
    
    # Prueba para verificar que se puede encontrar un usuario por su ID
    def test_detalles_incubacion_find(self):
    
        detalles_incubacion = self.__get_detalles_incubacion()
        detalles_incubacion_service.create(detalles_incubacion)

        detalles_incubacion_find = detalles_incubacion_service.get_by_id(1)
        self.assertIsNotNone(detalles_incubacion_find)
        self.assertEqual(detalles_incubacion_find.id, detalles_incubacion.id)
        self.assertEqual(detalles_incubacion.cant_huevos_inicial, self.cant_huevos_inicial_prueba)
    
    def __get_detalles_incubacion(self):
        detalles_incubacion = DetallesIncubacion()
        detalles_incubacion.cant_huevos_inicial = self.cant_huevos_inicial_prueba
        detalles_incubacion.cant_huevos_final = self.cant_huevos_final_prueba
        return detalles_incubacion
            
# Ejecutamos las pruebas si este script se ejecuta directamente
if __name__ == '__main__':
    unittest.main()