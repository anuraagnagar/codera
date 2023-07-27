from config.base import *

# MySQL Database Configuration.

DB_ENGINE = os.getenv("DB_ENGINE")

DB_USERNAME = os.getenv("DB_USERNAME")

DB_PASSWORD = os.getenv("DB_PASSWORD")

DB_HOST = os.getenv("DB_HOST")

DB_PORT = os.getenv("DB_PORT")

DB_NAME = os.getenv("DB_NAME")


try:
    SQLALCHEMY_DATABASE_URI = f"{DB_ENGINE}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
except Exception as e:
    print("Error: {}".format(e))


UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "assets", "uploads")

PROFILE_IMAGE_PATH = os.path.join(UPLOAD_FOLDER, 'profile')

COVER_IMAGE_PATH = os.path.join(UPLOAD_FOLDER, 'cover')

POST_THUMBNAIL_PATH = os.path.join(UPLOAD_FOLDER, 'thumbnail')