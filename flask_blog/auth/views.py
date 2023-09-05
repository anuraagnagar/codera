import re
import json
from datetime import timedelta

from flask import Markup as _
from flask import render_template as render
from flask import abort, flash, redirect, request, url_for, views

from flask_login import (
        current_user,
        login_user as login,
        logout_user as logout,
        login_required as LoginRequired
    )

from flask_blog.auth.services import (
        send_confirmation,
        send_reset_email,
        send_reset_password
    )
from flask_blog.extensions import database as db
from flask_blog.auth import (
        AccountVerifyForm,
        ChangePasswordForm,
        DeleteAccountForm,
        ForgotPasswordForm,
        EditProfileForm,
        LoginForm,
        RegisterForm,
        ResetEmailForm,
        ResetPasswordForm
    )

from flask_blog.utils import (
        generate_security_code,
        get_clean_username,
        get_clean_email,
        get_clean_password
    )

import config


with open("flask_blog/confi.json", "r") as c:
    params = json.load(c)["parameter"]


class BaseView(views.View):
    """
    A Base view class providing common functionality for
    all subclasses.
    """

    init_every_request = False

    def __init__(self, model=None, template=None):
        """
        Initializes the BaseView with the provided 
        model and template common.
        """
        self.model = model
        self.template = template


class RegisterView(BaseView):
    """
    A View class for handling User registration process.
    Username, Email and Password are required.
    Supports GET and POST methods.
    """

    def perform_create(self, form=None):
        username = form.data.get('username', None)
        email = form.data.get('email', None)
        password = form.data.get('password', None)

        try:
            user = self.model(
                    username=get_clean_username(username),
                    email=get_clean_email(email),
                    password=password
                )
            user.set_password(password)
            user.save()
            return send_confirmation(user)
        except Exception as e:
            flash("Something went wrong with the backend server.", category='error')
            return redirect(url_for('auth.register'))

    def process_signup(self, form=None):
        """
        Handle the request for user registration.
        """
        username = form.data.get('username', None)
        email = form.data.get('email', None)
        password = form.data.get('password', None)

        useremail_exist = self.model.get_user_by_email(email=email)
        username_exist = self.model.get_user_by_username(username=username)

        if useremail_exist:
            link = f"<a class='alert-link' href='{url_for('auth.login')}'>login</a>"
            flash(_("Your account already exists, Please {}.".format(link)), category='info')
        elif username_exist:
            flash("Username already exists, try another.", category='warning')
        elif not username or not email or not password:
            flash("Please fill out the form.", category='error')
        elif not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email):
            flash("Invalid email address.", category='error')
        elif not len(username) >= 5 and len(username) <= 30:
            flash("Username must between 5 to 30 Character.", category='error')
        elif not re.match(r"^[A-Za-z0-9_-]*$", username):
            flash("Username only contain alphabets, numbers and underscore.", category='info')
        elif not len(password) >= 8 or not len(password) <= 15:
            flash("Password must between 8 to 15 character.", category='error')
        elif not re.match(r"(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$", password):
            flash("Password should have at least one number, one uppercase, one lowercase, and one special character.", category='info')
        else:
            return self.perform_create(form=form)

        return redirect(url_for('auth.register'))

    def dispatch_request(self):
        """
        A method for handling GET and POST requests 
        for User registration.
        """
        form = RegisterForm()

        if current_user.is_authenticated:
            return redirect(url_for(config.AUTH_REDIRECT_URL))

        if form.validate_on_submit():
            return self.process_signup(form=form)

        return render(self.template, params=params, form=form) 


class LoginView(BaseView):
    """
    A View class for handling User login.
    Email and Password are required.
    Supports GET and POST methods.
    """

    def get_auth_user(self, email):
        """
        Get the authenticated User based on the provided email.
        Return the User instance if found, otherwise None.
        """
        return self.model.get_user_by_email(email=email)

    def get_login_redirect(self, message=None):
        """
        A method show flash message and redirecting
        to the 'login_redirect_url' route.
        """
        flash(message, category='success')
        login_redirect_url = request.args.get('redirect_url') or url_for('app.index')
        return redirect(login_redirect_url)

    def confirm_login(self, user, message=None):
        """
        A method for confirming User login and 
        saved in cookies and return
        'get_login_redirect()' method.
        """
        login(user, remember=True, duration=config.COOKIE_DURATION)
        return self.get_login_redirect(message=message)

    def process_login(self, user=None):
        try:
            user.security_code = generate_security_code()
            db.session.commit()
            return send_confirmation(user)
        except Exception as e:
            flash("Something went wrong with the backend server.", category='error')
            return redirect(url_for('auth.login'))

    def login_user(self, form=None):
        """
        Handle the request for User's login.
        """
        email = form.data.get('email', None)
        password = form.data.get('password', None)

        user = self.get_auth_user(email)

        if not user:
            flash("User account doesn't exists.", category='error')
        elif not user.check_password(password):
            reset_link = f"<a class='alert-link' href='{url_for('auth.forgot_password')}'>Forgot Password</a>"
            flash(_("Incorrect password, try again or click {} to reset it.".format(reset_link)), category='error')
        else:
            if user and not user.is_active():
                return self.process_login(user)
            
            return self.confirm_login(
                        user, message="You are successfully logged in."
                    )

        return redirect(url_for('auth.login'))

    def dispatch_request(self):
        """
        A method for handling GET and POST requests 
        for User login account.
        """
        form = LoginForm()

        if current_user.is_authenticated:
            return redirect(url_for(config.AUTH_REDIRECT_URL))
            
        if form.validate_on_submit():
            return self.login_user(form=form)

        return render(self.template, params=params, form=form)
     

class LogoutView(BaseView):
    """
    A View class for handling User logout.
    Supports GET method only.
    """

    def dispatch_request(self):
        """
        Handle the GET request for User logout.
        """
        if current_user.is_authenticated:
            logout()
            flash("You have logged out successfully.", category='success')
            return redirect(url_for(config.AUTH_REDIRECT_URL))

        return abort(404)


class VerifyAccountView(BaseView):
    """
    A View class for handling User account verification 
    via One Time Password(OTP) method.
    Supports GET and POST methods.
    """

    def authenticate_token(self, token, salt=None):
        """
        Authenticate the account verify token.
        Verify the token using the model's verify_token() method.
        Returns the token object if valid, otherwise None.
        """
        return self.model.verify_token(token=token, salt=salt)

    def confirm_account(self, auth_user=None, token=None):
        try:
            user = self.model.query.get_or_404(auth_user.id)
            user.active = True
            user.token = True
            login(user, remember=True, duration=config.COOKIE_DURATION)
            db.session.commit()
            flash("Welcome {}, You registered successfully.".format(user.username), category='success')
            return redirect(url_for('app.index'))
        except Exception as e:
            flash("Something went wrong with the backend server.", category='error')
            return redirect(url_for('auth.verify_account', token=token))

    def dispatch_request(self, token=None):
        """
        A method for handling GET and POST requests 
        for User account verification.
        """

        if not current_user.is_authenticated:
            user_token = self.authenticate_token(
                            token, salt='account_verify_token'
                        )
            
            if user_token and not user_token.is_expired() and not user_token.is_active():
                form = AccountVerifyForm()

                if form.validate_on_submit():
                    security_code = form.data.get('security_code', None)

                    if not user_token or user_token.is_expired():
                        return abort(404)
                    elif not security_code:
                        flash("Please fill out the form.", category='error')
                    elif not len(security_code) == 6:
                        flash("One Time Password(OTP) must be 6 digits.", category='error')
                    elif not (security_code == user_token.security_code):
                        flash("Your One Time Password(OTP) is incorrect.", category='error')
                    else:
                        return self.confirm_account(user_token, token=token)

                    return redirect(url_for('auth.verify_account', token=token))
         
                return render(self.template, params=params, token=token, form=form)

        return abort(404)
        

class ForgetPasswordView(BaseView):
    """
    A View class for send reset password request
    to User registered email address.
    Supports GET and POST methods.
    """

    def get_auth_user(self, email):
        """
        Get the authenticated User based on the provided email.
        Return the User instance if exists, otherwise None.
        """
        return self.model.get_user_by_email(email=email)

    def handle_request(self, form=None):

        email = form.data.get('email', None)

        user = self.get_auth_user(email)

        if user:
            return send_reset_password(user=user)
        
        flash("Email Address is not register with us.", category='error')
        return redirect(url_for('auth.forgot_password'))

    def dispatch_request(self):
        """
        A method for handling GET and POST requests 
        for sending Reset User's password.
        """
        form = ForgotPasswordForm()

        if form.validate_on_submit():
            return self.handle_request(form=form)

        return render(self.template, params=params, form=form)


class ResetPasswordView(BaseView):
    """
    A View class for handling password reset of User.
    Supports GET and POST methods.
    """

    def authenticate_token(self, token, salt=None):
        """
        Authenticate the reset password token.
        Verify the token using the User.verify_token() method.
        Returns the User object if token valid, otherwise None.
        """
        return self.model.verify_token(token, salt=salt)

    def confirm_reset(self, user=None, token=None, new_password=None):
        try:
            user.set_password(new_password)
            user.token = True
            if not current_user.is_authenticated:
                login(user, remember=True, duration=config.COOKIE_DURATION)
            db.session.commit()
            flash("Your password has been changed.", category='success')
            return redirect(url_for('app.index'))
        except Exception as e:
            flash("Something went wrong with the backend server.", category='error')
            return redirect(url_for('auth.reset_password', token=token))

    def dispatch_request(self, token=None):
        """
        A method for handlind GET and POST request for password reset.

        Render the password reset form validate and the update the User's 
        password if the token is valid and not expired.
        Otherwise return abort(404) method.
        """
        reset_token = self.authenticate_token(
                        token, salt='reset_password_token'
                    )

        if reset_token and not reset_token.is_expired():
            form = ResetPasswordForm()

            if form.validate_on_submit():
                password = form.data.get('password', None)
                confirm_password = form.data.get('confirm_password', None)

                if not reset_token or reset_token.is_expired():
                    return abort(404)
                elif not password or not confirm_password:
                    flash("Please fill out the form.", category='error')
                elif not (password == confirm_password):
                    flash("New password fields didn't match.", category='error')
                elif not len(password) >= 8 or not len(password) <= 15:
                    flash("Password must between 8 to 15 character.", category='error')
                elif not re.match(r"(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$", password):
                    flash("Password should have at least one number, one uppercase, one lowercase, and one special character.", category='info')
                else:
                    return self.confirm_reset(
                            user=reset_token, token=token, new_password=password
                        )
                
                return redirect(url_for('auth.reset_password', token=token))

            return render(self.template, params=params, token=token, form=form)
        
        return abort(404)
        

class ChangePasswordView(BaseView):
    """
    A View for change User password.
    Supports GET and POST methods.
    """

    decorators = [LoginRequired]

    def get_auth_user(self):
        """
        Get the authenticated User based on the current User's ID.
        Return the User if exists, or raise a 404 Not Found exception.
        """
        return self.model.query.get_or_404(current_user.id)

    def handle_change(self, form=None):
        old_password = form.data.get('old_password', None)
        new_password1 = form.data.get('new_password', None)
        new_password2 = form.data.get('new_password_confirm', None)

        user = self.get_auth_user()

        if not user.check_password(old_password):
            flash("Old password was entered incorrect.", category='error')
        elif not old_password or not new_password1 or not new_password2:
            flash("Please fill out the form.", category='error')
        elif not (new_password1 == new_password2):
            flash("New password fields didn't match.", category='error')
        elif not len(new_password1) >= 8 and not len(new_password1) <= 15:
            flash("Password must be between 8 to 15 character.", category='info')
        elif not re.match(r"(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$", new_password1):
            flash("Password should have at least one number, one uppercase, one lowercase, and one special character.", category='info')
        else:
            try:
                user.set_password(new_password1)
                db.session.commit()
                flash("Your password has been changed successfully.", category='success')
                return redirect(url_for('auth.change_password'))
            except Exception as e:
                flash("Something went wrong with the backend server.", category='error')
                return redirect(url_for('auth.change_password'))

        return redirect(url_for('auth.change_password'))

    def dispatch_request(self):
        """
        Handle the request to change the User's password.

        This method validates the change password form, checks the old password,
        enforces password requirements, and updates the User's password if valid.
        """
        form = ChangePasswordForm()

        if form.validate_on_submit():
            return self.handle_change(form=form)

        return render(self.template, params=params, form=form)


class ResetEmailView(BaseView):
    """
    A View class for sending reset request 
    of the user's email.
    Supports GET and POST methods.
    """

    decorators = [LoginRequired]

    def dispatch_request(self):
        """
        Handle the request for send a reset email to 
        the User's email address.
        """
        form = ResetEmailForm()

        if form.validate_on_submit():
            email = form.data.get('email', None)

            if not email:
                flash("Please fill out the form.", category='error')
            elif email == current_user.email:
                flash("Email is already verified with your account.", category='error')
            elif email and not re.match(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", email):
                flash("Invalid email address.", category='error')
            elif email in [user.email for user in self.model.query.all()]:
                flash("Email is already register with us.", category='error')
            else:
                return send_reset_email(email, current_user)

            return redirect(url_for('auth.update_email'))

        return render(self.template, params=params, form=form)


class ConfirmEmailView(BaseView):
    """
    A View class for confirm reset the user's new email.
    Supports GET and POST methods.
    """

    def authenticate_token(self, token, salt=None):
        """
        Authenticate the reset token for email address.
        Verify the token using the User.verify_token() method.
        Returns the User object if token valid, otherwise None.
        """
        return self.model.verify_token(token, salt=salt)
    
    def confirm_change(self, user, new_email=None):
        try:
            user.set_email(new_email)
            user.token = True
            db.session.commit()
            flash("Email Address was update successfully.", category='success')
            return redirect(url_for('app.index'))
        except Exception as e:
            flash("Something went wrong with the backend server.", category='error')
            return redirect(url_for('app.index'))

    def dispatch_request(self, email, token=None):
        """
        Handle the request for confirming user's reset 
        new email address.
        """
        reset_token = self.authenticate_token(
                        token, salt='reset_email_token'
                    )

        if reset_token and not reset_token.is_expired():

            if request.method == "POST":
                confirm = request.form.get('confirm', None)
                protect = request.form.get('csrf_token', None)

                return self.confirm_change(reset_token, email)
                
            return render(self.template, params=params, email=email, token=token)

        return abort(404)
        

class SendResendMailView(BaseView):
    """
    A View class for sending or resending email.
    """

    def __init__(self, model, token, salt):
        self.model = model
        self.token = token
        self.salt = salt

    def authenticate_token(self, token):
        """
        Verify the token using the model's verify_token() method.
        Returns the token object if valid, otherwise None.
        """
        return self.model.verify_token(self.token, salt=self.salt)

    def dispatch_request(self):
        """
        Handle the request for sending or resending email.
        """
        auth_token = self.authenticate_token(self.token)
        if auth_token:
            # Perform the necessary action for sending or resending email
            # based on the authenticated token.

            # Example:
            # send_email()

            flash("Email sent successfully.", category='success')
        else:
            flash("Invalid token.", category='error')

        return redirect(url_for('auth.login'))


class AccountView(BaseView):
    """
    A View class for handling User settings.
    Supports GET and POST methods.
    """

    decorators = [LoginRequired]

    def get_auth_user(self):
        """
        Get the authenticated User based on the current User's ID.
        Return the User if found, or raise a 404 Not Found exception.
        """
        return self.model.query.get_or_404(current_user.id)

    def confirm_request(self, form=None):
        """
        Confirms a request by validating the provided password
        and after perform the logout() delete user by 
        User.delete() method.
        """
        try:
            password = form.data.get('password', None)
            auth_user = self.get_auth_user()

            if auth_user and auth_user.check_password(password):
                logout()
                auth_user.delete()
                return redirect(url_for('app.index'))

            flash("You enter an incorrect password, Please try again.", category='error')
            return redirect(url_for('auth.settings'))
        except Exception as e:
            flash("Something went wrong with the backend server.", category='error')
            return redirect(url_for('auth.settings'))

    def dispatch_request(self):
        """
        A method for handling GET and POST request 
        for User settings.
        """
        form = DeleteAccountForm()

        if form.validate_on_submit():
            return self.confirm_request(form=form)
        
        return render(self.template, params=params, form=form)
            

class UserDetailView(BaseView):
    """
    A View class for Read and updates User and Profile model fields.
    Supports GET and POST methods.
    """

    decorators = [LoginRequired]

    def dispatch_request(self):

        form = EditProfileForm()
                
        if form.validate_on_submit():
            user = self.model.query.get_or_404(current_user.id)

            profile = user.get_profile()

            data = getattr(form, 'data')

            if data.get('username') in [user.username for user in self.model.query.all() if user != current_user]:
                flash('Username already exists, choose another.', category='error')
            elif not re.match(r"^[a-zA-Z ]*$", data.get('fullname')):
                flash("Fullname is contains only alphabet.", category='error')
            elif not re.match(r"^[a-z0-9_]*$", data.get('username')):
                flash("Username only contain alphabets, numbers and underscore.", category='error')
            elif len(data.get('username')) < 5 or len(data.get('username')) > 25:
                flash('Username must between 5 to 25 character.', category='error')
            elif not re.match(r"^[0-9]*$", data.get('mobile')) and not len(data.get('mobile')) == 10:
                flash("Your phone number is invalid .", category='error')
            else:
                try: 
                    username = data.get('username').lower()
                    user.set_username(username) 
                    profile.fullname = data.get('fullname')
                    profile.mobile = data.get('mobile')
                    profile.gender = data.get('gender')
                    profile.biodata = data.get('biodata')
                    profile.address = data.get('address')
                    profile.work = data.get('work')
                    profile.education = data.get('education')
                    profile.role = data.get('role')
                    profile.website_url = data.get('website')
                    profile.github_url = data.get('github')
                    profile.twitter_url = data.get('twitter')
                    profile.instagram_url = data.get('instagram')
                    profile.facebook_url = data.get('facebook')
                    profile.set_profile_image(data.get('profile_url'))
                    profile.set_cover_image(data.get('cover_url'))
                    db.session.commit()
                    flash("Your profile update successfully.", category='success')
                    return redirect(url_for('app.edit_profile'))
                except Exception as e:
                    flash("Something went wrong with the backend server.", category='error')
                    return redirect(url_for('app.edit_profile'))

            return redirect(url_for('app.edit_profile'))

        return render(self.template, params=params, form=form)


class GoogleLoginView(BaseView):
    """
    A View class for handling Google login.
    """
    pass


class GoogleLoginRedirectView(BaseView):
    pass


class GithubLoginView(BaseView):
    pass


class GithubLoginRedirectView(BaseView):
    pass
