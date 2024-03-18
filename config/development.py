from .base import *

DEBUG = True

# SQLite database for development environment.
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")

PROFILE_IMAGE_PATH = os.path.join(UPLOAD_FOLDER, "profile")

COVER_IMAGE_PATH = os.path.join(UPLOAD_FOLDER, "cover")

POST_THUMBNAIL_PATH = os.path.join(UPLOAD_FOLDER, "thumbnail")
