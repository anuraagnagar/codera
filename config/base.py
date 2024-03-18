import os
from datetime import timedelta
from dotenv import load_dotenv

# Base directory of our application project.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Loading environment variable using this method.
load_dotenv(dotenv_path=BASE_DIR, override=True)

# Site core configurations.

# Debug mode for Flask application.
DEBUG = False

# Testing mode for Flask application.
TESTING = False

# Secret key for Flask session management. It should be kept secret.
SECRET_KEY = os.getenv("SECRET_KEY")

# Bcrypt hashing rounds for password hashing.
BCRYPT_LOG_ROUNDS = 14

# Basic site information.

SITE_TITLE = "Codera"
SITE_URL = os.getenv("SITE_DOMAIN")

# flask-Caching configurations.

CACHE_TYPE = "SimpleCache"
CACHE_DEFAULT_TIMEOUT = 300

# WTF form CSRF configurations.

WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = os.getenv("CSRF_SECRET_KEY")
WTF_CSRF_TIME_LIMIT = 900

# Cookie configurations.

REMEMBER_COOKIE_DURATION = timedelta(days=30)
REMEMBER_COOKIE_HTTPONLY = True
REMEMBER_COOKIE_SECURE = True

# SQLAlchemy (ORM) Configurations.

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False

# Google OAuth Configuration.

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET_ID")

# Github OAuth Configuration.

GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET_ID")

# Constants for salting tokens used by URLTimedSerializer.

SALT_ACCOUNT_VERIFY = os.getenv("SALT_ACCOUNT_VERIFY", "verify_account")
SALT_RESET_PASSWORD = os.getenv("SALT_RESET_PASSWORD", "reset_password")
SALT_RESET_EMAIL_ADDRESS = os.getenv("SALT_RESET_EMAIL_ADDRESS", "reset_email")

# Default maximum age for URLTimedSerializer token.
URL_TOKEN_MAX_AGE_DEFAULT = 1800

# Email template path.

ACCOUNT_CONFIRM_TEMPLATE_PATH = "flask_blog/templates/email/verify_account_context.txt"
RESET_PASSWORD_TEMPLATE_PATH = "flask_blog/templates/email/reset_password_context.txt"
RESET_EMAIL_TEMPLATE_PATH = "flask_blog/templates/email/reset_email_context.txt"

# Mail Server Configuration.

MAIL_SERVER = os.getenv("MAIL_SERVER")
MAIL_PORT = int(os.getenv("MAIL_PORT"))
MAIL_USERNAME = os.getenv("MAIL_USERNAME")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
MAIL_USE_TLS = False
MAIL_USE_SSL = True

# Static files and image uploads.

# Folder for uploaded files.
UPLOAD_FOLDER = "uploads/"

TINY_KEY = os.getenv("TINYMCE_API_KEY")

# Default redirect URL after authentication.
AUTH_REDIRECT_URL = "app.index"
