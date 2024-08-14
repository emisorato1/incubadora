# Importamos las bibliotecas necesarias
import unittest
from flask import current_app
from app import create_app, db
from app.models.incubacion import Incubacion
from datetime import datetime


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
        
        self.fecha_entrada = datetime.strptime('10/05/2024', '%d/%m/%Y')
        self.fecha_salida = datetime.strptime('15/05/2024', '%d/%m/%Y')
        
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
    
    def test_incubacion(self):
        incubacion = self.__get_incubacion() 
        self.assertEqual(incubacion.fecha_entrada, self.fecha_entrada)
        self.assertEqual(incubacion.fecha_salida, self.fecha_salida)

    def test_incubacion_save(self):
    
        incubacion = self.__get_incubacion()
        db.session.add(incubacion)
        db.session.commit()
        
        self.assertEqual(incubacion.fecha_entrada, self.fecha_entrada)
        self.assertEqual(incubacion.fecha_salida, self.fecha_salida)

        
    def test_incubacion_delete(self):    
        
        incubacion = self.__get_incubacion()
        db.session.add(incubacion)
        db.session.commit()
        
        # Borrar el proceso
        db.session.delete(incubacion)
        db.session.commit()
        
        self.assertIsNone(incubacion.query.get(incubacion.id))
        
    def test_incubacion_all(self):
        
        incubacion = self.__get_incubacion()
        db.session.add(incubacion)
        db.session.commit()
        
        incubacion = Incubacion.query.all()
        self.assertGreaterEqual(len(incubacion), 1)
    
    def test_incubacion_find(self):
    
        incubacion = self.__get_incubacion()
        db.session.add(incubacion)
        db.session.commit()
    
        incubacion_find = Incubacion.find(1)
        self.assertIsNotNone(incubacion_find)
        self.assertEqual(incubacion_find.id, incubacion.id)
        self.assertEqual(incubacion_find.fecha_entrada, incubacion.fecha_entrada)
    
    
# Ejecutamos las pruebas si este script se ejecuta directamente
if __name__ == '__main__':
    unittest.main()
