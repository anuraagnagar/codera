import random
import unicodedata
import uuid

from werkzeug.utils import secure_filename


def generate_unique_id():
    """
    Generating a Unique ID string using
    uuid.uuid4() method.
    """
    return str(uuid.uuid4())


def get_clean_string(s):
    """
    A method for cleaning a text string like,
    removing spaces and returning in
    a lowerCase characters.
    """
    return str(s).replace(" ", "").lower()


def get_username_from_email(email):
    """
    Extracts a username from an email address.
    """
    return email.split("@")[0]


def get_filename_from_path(file_path):
    """
    Extracts and returns the filename from the
    given file path.
    """
    path = str(file_path).split("\\")
    return path[-1]


def generate_unique_filename(filename):
    """
    Generate a unique and secure filename using
    secure_filename() method and UUID.
    """
    return secure_filename(generate_unique_id() + filename)


def generate_security_code():
    """
    A Method for generating a random (6 DIGIT)
    number for One Time Password(OTP).
    """
    return str(random.randint(100000, 999999))
