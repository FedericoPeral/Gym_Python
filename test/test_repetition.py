import unittest
from flask import current_app
from app import create_app, db
from app.models import Repetition

class RepetitionTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_repetition(self):
        repetition = Repetition(workout_id=1, exercise_id=1, series_number=1, num_repetitions=[10, 12, 8], peso=50.0)
        self.assertEqual(repetition.workout_id, 1)
        self.assertEqual(repetition.exercise_id, 1)
        self.assertEqual(repetition.series_number, 1)
        self.assertEqual(repetition.num_repetitions, [10, 12, 8])
        self.assertEqual(repetition.peso, 50.0)

if __name__ == '__main__':
    unittest.main()
