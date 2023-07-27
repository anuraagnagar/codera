from config.base import *

DEBUG = True

TESTING = True

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")

UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "assets", "uploads")

PROFILE_IMAGE_PATH = os.path.join(UPLOAD_FOLDER, "profile")

COVER_IMAGE_PATH = os.path.join(UPLOAD_FOLDER, "cover")

POST_THUMBNAIL_PATH = os.path.join(UPLOAD_FOLDER, "thumbnail")
