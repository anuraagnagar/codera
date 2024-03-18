import os

ENVIRON = os.environ["FLASK_ENV"]  # get environment status.

try:
    if ENVIRON == "production":
        from .production import *
    elif ENVIRON == "development":
        from .development import *
    else:
        raise ValueError("")
except ImportError as err:
    raise ImportError(err)
