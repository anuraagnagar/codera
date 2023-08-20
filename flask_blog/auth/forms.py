from wtforms.fields import (
        BooleanField,
        EmailField,
        PasswordField,
        SelectField,
        StringField,
        SubmitField, 
        TextAreaField,
        URLField
    )
from wtforms.validators import (
        DataRequired,
        Email,
        Length
    )

from flask_wtf import FlaskForm
from flask_wtf.file import (
        FileAllowed,
        FileField,
        FileRequired,
        FileSize,
    )

from flask_blog.auth import Users
from flask_blog.auth.validators import Unique


class RegisterForm(FlaskForm):
    """
    A FlaskForm class for User registration.
    """

    username = StringField(
            "Username", validators=[
                DataRequired(), Length(5, 30),
                Unique(Users, Users.username, 'Username already exists.')
            ])
    email = EmailField(
            "Email Address", validators=[
                Email(), DataRequired(), Length(8, 150),
                Unique(Users, Users.email, 'User account with this email already exists.')             
            ])
    password = PasswordField("Password", validators=[DataRequired(), Length(8, 15)])
    check = BooleanField("I accept all terms of services.", validators=[DataRequired()])
    submit = SubmitField("Continue")


class LoginForm(FlaskForm):
    """
    A FlaskForm class for User Login account.
    """

    email = EmailField("Email Address", validators=[DataRequired(), Length(8, 150)])
    password = PasswordField("Password", validators=[DataRequired(), Length(8, 15)])
    check = BooleanField("Remember me", validators=[DataRequired()])
    submit = SubmitField("Continue")


class AccountVerifyForm(FlaskForm):
    """
    A FlaskForm class for User account verification
    using OTP code.
    """

    security_code = StringField("One Time Password(OTP)", validators=[DataRequired(), Length(min=6, max=6)])
    check = BooleanField("I accept all terms of services.", validators=[DataRequired()])
    submit = SubmitField("Confirm Account")


class ForgotPasswordForm(FlaskForm):
    """
    A FlaskForm class for User password recovery.
    """

    email = EmailField("Email Address", name="email", validators=[DataRequired(), Length(8, 150), Email()])
    check = BooleanField("I accept all terms of services.", validators=[DataRequired()])
    submit = SubmitField("Send Reset Mail")


class ResetPasswordForm(FlaskForm):
    """
    A FlaskForm class for User reset new password.
    """

    password = PasswordField("Password", validators=[DataRequired(), Length(8, 15)])
    confirm_password = PasswordField(
                    "Confirm Password", 
                    validators=[DataRequired(), Length(8, 15)]
                )
    check = BooleanField("Remember me", validators=[DataRequired()])
    submit = SubmitField("Submit")


class ResetEmailForm(FlaskForm):
    """
    A FlaskForm class for resetting new
    User email address.
    """

    email = EmailField("Email Address", name="email", validators=[DataRequired(), Length(8, 150), Email()])
    check = BooleanField("I accept all terms of services.", validators=[DataRequired()])
    submit = SubmitField("Send Confirmatiom Mail")    


class ChangePasswordForm(FlaskForm):
    """
    A FlaskForm class for changing User password.
    """

    old_password = PasswordField("Old Password", name="password", validators=[DataRequired(), Length(8, 15)])
    new_password = PasswordField("New Password", name="password", validators=[DataRequired(), Length(8, 15)])
    new_password_confirm = PasswordField(
                        "Confirm New Password", name="password",
                        validators=[DataRequired(), Length(8, 15)]
                    )
    check = BooleanField("Remember me", validators=[DataRequired()])
    submit = SubmitField("Set Password")


class EditProfileForm(FlaskForm):
    """
    A FlaskForm class for represent User profile.
    """

    fullname = StringField("Fullname")
    username = StringField("Username", validators=[DataRequired(), Length(6, 30)])
    mobile = StringField("Phone Number")
    gender = SelectField("Gender", 
                choices=['Select...', 'Male', 'Female', 'Other'],
                default='Select...'
            )
    biodata = TextAreaField("Biodata", validators=[Length(max=200)])
    address = StringField("Address", validators=[Length(max=100)])
    work = StringField("Work", validators=[Length(max=100)])
    education = StringField("Education", validators=[Length(max=100)])
    role = StringField("Role", validators=[Length(max=100)])
    profile_image = FileField("Profile Image",
                validators=[
                    FileAllowed(["jpg", "jpeg", "png"], 'Images Only'),
                    FileSize(max_size=3000000)
                ]
            )
    cover_image = FileField("Upload Cover Image",
                validators=[
                    FileAllowed(["jpg", "jpeg", "png"], 'Images Only'),
                    FileSize(max_size=3000000)
                ]
            )
            
    website_url = URLField("Website Url", validators=[Length(max=150)])
    github_url = URLField("Github Url", validators=[Length(max=150)])
    twitter_url = URLField("Twitter Url", validators=[Length(max=150)])
    instagram_url = URLField("Instagram Url", validators=[Length(max=150)])
    facebook_url = URLField("Facebook Url", validators=[Length(max=150)])
    submit = SubmitField("Update Profile")


class DeleteAccountForm(FlaskForm):
    """
    A FlaskForm class for deleting User's account.
    """

    password = PasswordField(
            "Confirm Your Password", name="password",
            validators=[DataRequired(), Length(8, 15)]
        )
    submit = SubmitField("Delete Account")
    