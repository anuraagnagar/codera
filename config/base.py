from dotenv import load_dotenv
from datetime import timedelta
import os

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Site Configuration

SITE_TITLE = "CodeCircle"

DEBUG = False

TESTING = False

SECRET_KEY = os.getenv("SECRET_KEY")

WTF_CSRF_ENABLED = True

WTF_CSRF_SECRET_KEY = os.getenv("CSRF_SECRET_KEY")

WTF_CSRF_TIME_LIMIT = 900

COOKIE_DURATION = timedelta(days=30)

TINY_KEY = os.getenv("TINYMCE_API_KEY")

AUTH_REDIRECT_URL = "app.index"


# Database SQLAlchemy Configuration.

SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_ECHO = False


# Mail Server Configuration

MAIL_SERVER = os.getenv("MAIL_SERVER")

MAIL_PORT = int(os.getenv("MAIL_PORT"))

MAIL_USERNAME = os.getenv("MAIL_USERNAME")

MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

MAIL_USE_TLS = bool(os.getenv("MAIL_USE_TLS"))

MAIL_USE_SSL = bool(os.getenv("MAIL_USE_SSL"))

MAIL_DEFAULT_SENDER = MAIL_USERNAME