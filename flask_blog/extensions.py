from flask_admin import Admin
from flask_babel import Babel
from flask_bcrypt import Bcrypt
from flask_wtf import CSRFProtect
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_migrate import Migrate
from flask_script import Manager
from flask_tinymce import TinyMCE

"""
The following 'Flask' extensions used in our application.

"""

# admin (Admin): An admin panel for management.
admin = Admin()

# babel (Babel): An extension for internationalization transalations.
babel = Babel()

# bycrpt (Bcrypt): Bcrypt for hashing user passwords. 
bycrpt = Bcrypt()

# csrf (CSRFProtect): CSRF protection for form data.
csrf = CSRFProtect()

# login_manager (LoginManager): for User login management.
login_manager = LoginManager()

# database (SQLAlchemy): An ORM for working with the database.
database = SQLAlchemy()

# mail (Mail): An extension for sending emails.
mail = Mail()

# migration (Migrate): An extension for changing and updating the database.
migration = Migrate()

# tinymce (TinyMCE): A rich text editor for editing content.
tinymce = TinyMCE()

