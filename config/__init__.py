from .base import SITE_TITLE
from .base import COOKIE_DURATION
from .base import SECRET_KEY
from .base import MAIL_USERNAME
from .base import AUTH_REDIRECT_URL
from .production import UPLOAD_FOLDER
from .production import POST_THUMBNAIL_PATH
from .production import PROFILE_IMAGE_PATH
from .production import COVER_IMAGE_PATH

__all__ = [
    "COOKIE_DURATION",
    "SECRET_KEY",
    "MAIL_USERNAME",
    "AUTH_REDIRECT_URL",
    "UPLOAD_FOLDER"
]