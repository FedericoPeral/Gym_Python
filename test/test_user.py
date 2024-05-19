import unittest
from flask import current_app
from app import create_app, db
from app.models import User

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
    
    def test_user(self):
        # Creamos un objeto User
        user = User(username='test', password='test1234', email='test@test.com')

        # Verificamos si los atributos se han establecido correctamente
        self.assertEqual(user.username, 'test')
        self.assertEqual(user.password, 'test1234')
        self.assertEqual(user.email, 'test@test.com')

if __name__ == '__main__':
    unittest.main()
