# Importamos las bibliotecas necesarias
import os
import unittest
from flask import current_app
from app import create_app, db
from app.models.user import User
from app.services import UserService

user_service = UserService()

# Definimos la clase de prueba para el modelo User utilizando unittest
class UserTestCase(unittest.TestCase):
    """
    Test User model
    Necesitamos aplicar principios como DRY (Don't Repeat Yourself) y KISS (Keep It Simple, Stupid).
    YAGNI (You Aren't Gonna Need It) y SOLID (Single Responsibility Principle).
    """

    # Configuramos el entorno de prueba
    def setUp(self):
        
        os.environ['FLASK_CONTEXT'] = 'testing'

        # Creamos la aplicación y el contexto de la aplicación para pruebas
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        # Creación de todas las tablas en la base de datos
        db.create_all()
        
        self.user_name_prueba = 'nombre'
        self.password_prueba = '12345'
        self.role_prueba = 'tecnico'
        
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
    def test_user(self):
        user = self.__get_user()        
        self.assertEqual(user.user_name, self.user_name_prueba)
        self.assertEqual(user.password, self.password_prueba)   
        self.assertEqual(user.role, self.role_prueba)
    
    # Prueba para verificar que el usuario se guarda correctamente en la base de datos
    def test_user_save(self):
    
        user = self.__get_user()
        user_service.save(user)

        self.assertGreaterEqual(user.id, 1)
        self.assertEqual(user.user_name, self.user_name_prueba)
        self.assertEqual(user.password, self.password_prueba)   
        self.assertEqual(user.role, self.role_prueba)
        
    # Prueba para verificar que el usuario se elimina correctamente de la base de datos
    def test_user_delete(self):
        
        user = self.__get_user()
        user_service.save(user)

        # Borrar el usuario
        user_service.delete(user.id)
        self.assertIsNone(user_service.find(user))
    
    # Prueba para verificar que se pueden obtener todos los usuarios
    def test_user_all(self):
    
        user = self.__get_user()
        user_service.save(user)

        users = user_service.all()
        self.assertGreaterEqual(len(users), 1)
    
    # Prueba para verificar que se puede encontrar un usuario por su ID
    def test_user_find(self):
    
        user = self.__get_user()
        user_service.save(user)

        user_find = user_service.find(1)
        self.assertIsNotNone(user_find)
        self.assertEqual(user_find.id, user.id)
        self.assertEqual(user_find.role, user.role)
        
    def __get_user(self):
        user = User()
        user.user_name = self.user_name_prueba
        user.password = self.password_prueba
        return user

# Ejecutamos las pruebas si este script se ejecuta directamente
if __name__ == '__main__':
    unittest.main()
