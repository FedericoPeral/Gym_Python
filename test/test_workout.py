import unittest
from flask import current_app
from app import create_app, db
from app.models import Workout

class WorkoutTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_workout(self):
        workout = Workout(user_id=1, date_time='2022-04-25 10:00:00', name_workout='Leg Day')
        self.assertEqual(workout.user_id, 1)
        self.assertEqual(workout.date_time, '2022-04-25 10:00:00')
        self.assertEqual(workout.name_workout, 'Leg Day')

if __name__ == '__main__':
    unittest.main()
