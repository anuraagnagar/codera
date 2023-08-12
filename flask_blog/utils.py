from werkzeug.utils import secure_filename
import unicodedata
import random
import uuid


def generate_unique_id():
    """
    A Method for generating a Unique ID
    using uuid.uuid4() method.
    """
    return str(uuid.uuid4())

def get_clean_username(username):
    """
    A method for cleaning a User's username like,
    removing spaces and returning in 
    a lowerCase characters.
    """
    return str(username).replace(" ", "").lower()

def get_clean_email(email):
    """
    A method for cleaning a User's email like,
    removing spaces and returning in 
    a lowerCase characters.
    """
    clean_email = str(email).replace(" ", "")
    return clean_email.lower()

def get_clean_password(password):
    """
    A method for cleaning a User's password like,
    removing extraspaces spaces.
    """
    clean_password = str(password).replace(" ", "")
    return clean_password.lower()

def generate_unique_filename(filename):
    """
    Generate a unique and secure filename using
    secure_filename() method and UUID.
    """
    return secure_filename(
        generate_unique_id() + filename
    )

def generate_security_code():
    """
    A Method for generating a random '6 DIGIT'
    number for One Time Password(OTP). 
    """
    return str(random.randint(100000, 999999))