from app.models import Exercise
from marshmallow import fields, Schema, post_load

class ExerciseSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    description = fields.String(required=True)
    workout_id = fields.Integer(required=True)

    @post_load
    def make_exercise(self, data, **kwargs):
        return Exercise(**data)