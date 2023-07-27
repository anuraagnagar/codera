from wtforms.fields import (
        BooleanField,
        EmailField,
        StringField,
        SubmitField,
        TextAreaField
    )
from wtforms.validators import (
        DataRequired,
        Length
    )
    
from flask_wtf import FlaskForm


class ContactForm(FlaskForm):
    """
    A FlaskForm class for represent contact form.
    """

    name = StringField("Name", validators=[DataRequired(), Length(5, 50)])
    email = EmailField("Email Address", validators=[DataRequired(), Length(8, 150)])
    mobile = StringField("Phone Number", validators=[DataRequired(), Length(max=10)])
    message = TextAreaField("Message", validators=[DataRequired()])
    check = BooleanField("I agree & accept all the terms of services.", validators=[DataRequired()])
    submit = SubmitField("Submit")
