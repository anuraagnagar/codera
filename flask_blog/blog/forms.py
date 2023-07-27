from wtforms.fields import (
        BooleanField,
        SelectField,
        StringField,
        SubmitField,
        TextAreaField,
        URLField
    )
from wtforms.validators import (
        DataRequired,
        Length
    )
    
from flask_wtf import FlaskForm
from flask_wtf.file import (
        FileAllowed,
        FileField,
        FileRequired,
        FileSize
    )

from flask_blog.helpers import post_category


class CreatePostForm(FlaskForm):
    """
    A FlaskForm class for adding new blogpost.
    """

    category = SelectField("Select Category", 
                choices=post_category(),
                default='Select...'
            )
    title = StringField("Title", validators=[DataRequired(), Length(max=100)])
    subtitle = StringField("Sub Title", validators=[DataRequired(), Length(max=150)])
    content = TextAreaField("Content", validators=[DataRequired()])
    image_file = FileField("Add Cover Image", validators=[
                FileRequired(),
                FileSize(max_size=3000000)
            ])
    submit = SubmitField("Add Post")


class EditPostForm(FlaskForm):
    """
    A FlaskForm class for editing existing blogpost.
    """

    category = SelectField("Select Category", 
                choices=post_category(),
                default='Select...'
            )
    title = StringField("Title", validators=[DataRequired(), Length(max=100)])
    subtitle = StringField("Sub Title", validators=[DataRequired(), Length(max=150)])
    content = TextAreaField("Content", validators=[DataRequired()])
    image_file = FileField("Change Cover Image", validators=[
                FileSize(max_size=3000000)
            ])
    submit = SubmitField("Submit Changes")


class PostCommentForm(FlaskForm):
    """
    A FlaskForm class for posting comments 
    on a blogpost.
    """

    content = TextAreaField("Add Comment", validators=[DataRequired(), Length(min=3)])
    submit = SubmitField("Submit")

