from wtforms import Form, StringField, validators, FileField, ValidationError


class SplineInputFormValidator(Form):
    x = StringField('X', [validators.Length(min=1, max=2500), validators.InputRequired()])
    y = StringField('Y', [validators.Length(min=1, max=2500), validators.DataRequired()])
    k = StringField('K', [validators.Length(min=1, max=1), validators.DataRequired()])
    image = FileField('Image', [])

    def validate_x(form, field):
        if len(field.data) < 1:
            raise ValidationError('Name must be less than 50 characters')