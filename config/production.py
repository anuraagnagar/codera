from sqlalchemy.engine import URL

from .base import *

DB_ENGINE = os.getenv("DATABASE_ENGINE")
DB_USERNAME = os.getenv("DATABASE_USERNAME")
DB_PASSWORD = os.getenv("DATABASE_PASSWORD")
DB_HOST = os.getenv("DATABASE_HOST")
DB_PORT = os.getenv("DATABASE_PORT")
DB_NAME = os.getenv("DATABASE_NAME")

url_database = URL.create(
    DB_ENGINE,
    username=DB_USERNAME,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
)

# PostgreSQL Database configuration for production environment.
try:
    SQLALCHEMY_DATABASE_URI = url_database
except Exception as e:
    print("Error: {}".format(e))


PROFILE_IMAGE_PATH = os.path.join(UPLOAD_FOLDER, "profile")

COVER_IMAGE_PATH = os.path.join(UPLOAD_FOLDER, "cover")

POST_THUMBNAIL_PATH = os.path.join(UPLOAD_FOLDER, "thumbnail")
