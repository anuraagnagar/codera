from flask import Blueprint, render_template as render, redirect, request, url_for, flash, views
from flask_login import (
        login_required as LoginRequired,
        current_user,
        login_user,
        logout_user
    )

from flaskblog import database as db
from flaskblog.auth.models import (
        Users,
        Profile
    )
from flaskblog.app.models import (
        Contact,
        Blogpost,
        Likepost,
        Savepost,
        Comment,
        Reply
    )
from flaskblog.exception import (
        page_not_found as PageNotFound
    )

from datetime import timedelta
import json
import re


with open("flaskblog/confi.json", "r") as c:
    params = json.load(c)["parameter"]


class AdminLoginView(views.MethodView):

    init_every_request = False
    template = "login.html"
    model = Users
    
    def get(self):
        if current_user.is_authenticated and current_user.is_admin():
            return redirect(url_for('admin.index'))
        return render(self.template)
    
    def post(self):
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        
        _username_exist = self.model.query.filter_by(username=username).first()
        _email_exist = self.model.query.filter_by(email=username).first()

        user = _username_exist or _email_exist

        if not user:
            flash("Invalid credentials provided.", category='error')
        elif user and not user.is_admin():
            flash("You are not authorized to login.", category='error')
        elif user and not user.check_password(password):
            flash("Incorrect password, try again.", category='error')
        else:
            if user and user.is_admin():
                try:
                    login_user(user, remember=True, duration=timedelta(days=30))
                    flash("You are successfully login.", category='success')
                    return redirect(url_for('admin.index'))
                except Exception as e:
                    flash("Something went wrong with backend server.")
                    return redirect(url_for('admin.login'))

        return redirect(url_for('admin.login'))


class AdminLogoutView(views.View):

    init_every_request = False
    template = None

    def dispatch_request(self):
        if current_user.is_authenticated and current_user.is_admin():
            logout_user()
            flash("You logout successfully.", category='success')
            return redirect(url_for('admin.login'))

        return PageNotFound()


class AdminHomeView(views.View):

    template = "index.html"
    model = Users

    def dispatch_request(self):
        if current_user.is_authenticated and current_user.is_admin():
            user = self.model.query.get_or_404(current_user.id)
            return render(self.template, current_user=current_user)

        flash("Please login your account.", category='error')
        return redirect(url_for('admin.login'))


class AdminChangePasswordView(views.MethodView):

    template = "changepassword.html"
    model = Users

    def get(self):
        if current_user.is_authenticated and current_user.is_admin():
            return render(self.template)
        return PageNotFound()

    def post(self):
        if current_user.is_authenticated and current_user.is_admin():

            old_password = request.form.get('old_password')
            new_password1 = request.form.get('new_password1')
            new_password2 = request.form.get('new_password2')

            user = self.model.query.get_or_404(current_user.id)

            if not user.check_password(old_password):
                flash("Old password was entered incorrect.", category='error')
            elif not (new_password1 == new_password2):
                flash("New password fields didn't match.", category='error')
            elif not len(new_password1) >= 8 and not len(new_password1) <= 15:
                flash("Password must be between 8 to 15 character.", category='error')
            elif not re.match(r"(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$", new_password1):
                flash("Password must have at least one number, one uppercase, one lowercase, and one special character.", category='info')
            else:
                try:
                    user.set_password(new_password1)
                    db.session.commit()
                    flash("Your password changed successfully.", category='success')
                    return redirect(url_for('admin.index'))
                except Exception as e:
                    flash("Something went wrong with backend server.", category='error')
                    return redirect(url_for('admin.change_password'))

            return redirect(url_for('admin.change_password'))

        return PageNotFound()


class ShowUserView(views.MethodView):

     template = "showusers.html"
     model = Users

     def get(self):
        if current_user.is_authenticated and current_user.is_admin():
            users = self.model.query.order_by(Users.created.desc()).all() 
            return render(self.template, users=users)
        return PageNotFound()


class AddUserView(views.MethodView):

    template = "adduser.html"
    model = Users

    def get(self):
        if current_user.is_authenticated and current_user.is_admin():
            return render(self.template)
        return PageNotFound()

    def post(self):
        if current_user.is_authenticated and current_user.is_admin():
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')
            active = request.form.get('active') or False
            superuser = request.form.get('superuser') or False

            _useremail_exist = self.model.query.filter_by(email=email).first()
            _username_exist = self.model.query.filter_by(username=username).first()

            if _useremail_exist:
                flash("User with that email already exists.", category='error')
            elif _username_exist:
                flash("Username already taken, choose another.", category='error')
            elif not username or not email or not password:
                flash("Please fill out the form.", category='error')
            elif not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email):
                flash("Invalid email address.", category='error')
            elif not len(username) >= 5 and not len(username) <= 30:
                flash("Username must between 5 to 30 Character.", category='error')
            elif not re.match(r"^[a-z0-9_]*$", username):
                flash("Username only contain alphabets, numbers and underscore.", category='info')
            elif not len(password) >= 8 or not len(password) <= 15:
                flash("Password must between 8 to 15 character.", category='error')
            elif not re.match(r"(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$", password):
                flash("Password should have at least one number, one uppercase, one lowercase, and one special character.", category='info')
            else:
                try:
                    user = self.model(
                            username=username.lower(),
                            email=email.lower(),
                            password=password,
                            active=bool(active),
                            superuser=bool(superuser)
                        )
                    user.set_password(password)
                    db.session.add(user)
                    db.session.commit()
                    flash(f"User '{user.username}' was added successfully.", category='success')
                    return redirect(url_for('admin.show_users'))
                except Exception as e:
                    flash("Something went wrong with backend server.", category='error')
                    return redirect(url_for('admin.add_user'))

            return redirect(url_for('admin.add_user'))

        return PageNotFound()


class EditUserView(views.MethodView):
    
    template = "edituser.html"
    model = Users

    def get(self, username=None):
        if current_user.is_authenticated and current_user.is_admin():
            user = self.model.query.filter_by(username=username).first()

            if not user:
                flash(f"User with username '{username}' doesn't exist.", category='error')
                return redirect(url_for('admin.index')) 
            return render(self.template, user=user)

        return PageNotFound()

    def post(self, username=None):
        user = self.model.query.filter_by(username=username).first()

        if not user:
            flash(f"User with Username '{username}' doesn't exist.", category='error')
            return redirect(url_for('admin.index')) 

        if current_user.is_authenticated and current_user.is_admin():
            username = request.form.get('username')
            email = request.form.get('email')
            active = request.form.get('active') or False
            superuser = request.form.get('superuser') or False

            if email in [_user.email for _user in Users.query.all() if _user != user]:
                flash("User with that email already exists.", category='error')
            elif username in [_user.username for _user in Users.query.all() if _user != user]:
                flash("Username already taken, choose another.", category='error')
            elif not username or not email:
                flash("Please fill out the form.", category='error')
            elif not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email):
                flash("Invalid email address.", category='error')
            elif not len(username) >= 5 and len(username) <= 30:
                flash("Username must between 5 to 30 Character.", category='error')
            elif not re.match(r"^[a-z0-9_]*$", username):
                flash("Username only contain alphabets, numbers and underscore.", category='info')
            else:
                try:
                    user.username = username
                    user.email = email
                    user.active = bool(active)
                    user.superuser = bool(superuser)
                    db.session.commit()
                    flash(f"User '{user.username}' was update successfully.", category='success')
                    return redirect(url_for('admin.show_users'))
                except Exception as e:
                    flash("Something went wrong with backend server.", category='error')
                    return redirect(url_for('admin.show_users'))

            return redirect(url_for('admin.edit_user', username=user.username))

        return PageNotFound()


class DeleteUserView(views.View):

    template = None
    model = Users

    def dispatch_request(self, username=None):
        if current_user.is_authenticated and current_user.is_admin():
            auth_user = self.model.query.filter_by(username=username).first()

            if auth_user:
                try:
                    db.session.delete(auth_user)
                    db.session.commit()
                    flash(f"User with username '{username}' was successfully deleted.", category='success')
                    return redirect(url_for('admin.show_users'))
                except Exception as e:
                    flash("Something went wrong with backend server.", category='error')
                    return redirect(url_for('admin.edit_user', username=username))

            return redirect(url_for('admin.index'))
            
        return PageNotFound()


class ShowProfileView(views.MethodView):
    pass


class AddProfileView(views.MethodView):
    pass


class EditProfileView(views.MethodView):
    pass


class DeleteProfileView(views.MethodView):
    pass


class ShowBlogpostView(views.MethodView):
    pass


class AddBlogpostView(views.MethodView):
    pass


class EditBlogpostView(views.MethodView):
    pass


class DeleteBlogpostView(views.MethodView):
    pass


class ShowContactView(views.MethodView):
    pass


class AddContactView(views.MethodView):
    pass


class EditContactView(views.MethodView):
    pass


class DeleteContactView(views.MethodView):
    pass


class ShowCommentView(views.MethodView):
    pass


class AddCommentView(views.MethodView):
    pass


class EditCommentView(views.MethodView):
    pass


class DeleteCommentView(views.MethodView):
    pass


class ShowLikesView(views.MethodView):
    pass


class AddLikesView(views.MethodView):
    pass


class EditLikesView(views.MethodView):
    pass


class DeleteLikesView(views.MethodView):
    pass


class ShowSavesView(views.MethodView):
    pass


class AddSavesView(views.MethodView):
    pass


class EditSavesView(views.MethodView):
    pass


class DeleteSavesView(views.MethodView):
    pass


class ShowReplyView(views.MethodView):
    pass


class AddReplyView(views.MethodView):
    pass


class EditReplyView(views.MethodView):
    pass


class DeleteReplyView(views.MethodView):
    pass
