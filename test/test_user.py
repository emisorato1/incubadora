# Importamos las bibliotecas necesarias
import unittest
from flask import current_app
from app import create_app, db
from app.models.user import User

# Definimos la clase de prueba para el modelo User utilizando unittest
class UserTestCase(unittest.TestCase):
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
    
        user = User()
        user.user_name = 'cardozo'
        user.password = 'Qvv3r7y'
        user.role = 'tecnico'

        self.assertTrue(user.user_name, 'cardozo')
        self.assertTrue(user.password, 'Qvv3r7y')   
        self.assertTrue(user.role, 'tecnico')
    
    # Prueba para verificar que el usuario se guarda correctamente en la base de datos
    def test_user_save(self):
    
        user = User()
        user.user_name = 'cardozo'
        user.password = 'Qvv3r7y'
        user.role = 'tecnico'

        user.save()
        self.assertGreaterEqual(user.id, 1)
        self.assertTrue(user.user_name, 'cardozo')
        self.assertTrue(user.password, 'Qvv3r7y')   
        self.assertTrue(user.role, 'tecnico')
        
    # Prueba para verificar que el usuario se elimina correctamente de la base de datos
    def test_user_delete(self):

        user = User()
        user.user_name = 'cardozo'
        user.password = 'Qvv3r7y'
        user.role = 'tecnico'

        user.save()

        # Borramos el usuario
        user.delete()
        self.assertIsNone(User.find(user.id))
    
    # Prueba para verificar que se pueden obtener todos los usuarios
    def test_user_all(self):
    
        user = User()
        user.user_name = 'cardozo'
        user.password = 'Qvv3r7y'
        user.role = 'tecnico'
        user.save()

        users = User.all()
        self.assertGreaterEqual(len(users), 1)
    
    # Prueba para verificar que se puede encontrar un usuario por su ID
    def test_user_find(self):
    
        user = User()
        user.user_name = 'cardozo'
        user.password = 'Qvv3r7y'
        user.role = 'tecnico'
        user.save()

        user_find = User.find(1)
        self.assertIsNotNone(user_find)
        self.assertEqual(user_find.id, user.id)
        self.assertEqual(user_find.role, user.role)

# Ejecutamos las pruebas si este script se ejecuta directamente
if __name__ == '__main__':
    unittest.main()
