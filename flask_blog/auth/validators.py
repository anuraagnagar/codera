from flask import flash
from wtforms.validators import ValidationError


class Unique(object):

    def __init__(self, model, field, message):
        self.model = model
        self.field = field
        self.message = message

    def __call__(self, form, field):
        object_exist = self.model.query.filter(self.field == field.data).first()
        if object_exist:
            flash(self.message, category='info')