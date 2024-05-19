import unittest
from flask import current_app
from app import create_app, db
from app.models import Exercise

class ExerciseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_exercise(self):
        exercise = Exercise(name='Squats', description='Leg exercise', workout_id=1)
        self.assertEqual(exercise.name, 'Squats')
        self.assertEqual(exercise.description, 'Leg exercise')
        self.assertEqual(exercise.workout_id, 1)

if __name__ == '__main__':
    unittest.main()

