import logging
import random
import string
import unicodedata
import uuid

from slugify import slugify
from werkzeug.utils import secure_filename
from flask import current_app


def get_clean_string(s):
    """
    A method for cleaning a text string like,
    removing spaces and returning in
    a lowerCase characters.
    """
    return str(s).replace(" ", "").lower()


def get_full_url(url_path=None):
    """
    Construct a full URL by combining the site domain
    and the given URL path.

    Example:
        >>> get_full_url("/account/login")
        >>> 'https://www.example.com/account/login'
    """
    try:
        domain = current_app.config["SITE_URL"]
    except Exception as err:
        raise ValueError(
            "'SITE_URL' not found in current_app.config. Error :  %s" % err
        )

    return "{domain}{url_path}".format(domain=domain, url_path=url_path)


def get_username_from_email(email):
    """
    Extract the username from an email address.

    Example:
        >>> get_username_from_email("johndoe@example.com")
        >>> 'johndoe'
    """
    return str(email).split("@")[0]


def get_filename_from_path(file_path):
    """
    Extracts and returns the filename from the
    given file path.

    Example:
        >>> get_filename_from_path("C:\\path\\to\\profile.jpg")
        >>> 'profile.jpg'
    """
    path = str(file_path).split("\\")
    return path[-1]


def generate_unique_filename(filename):
    """
    Generate a unique and secure filename using
    secure_filename() method and UUID module.

    Example:
        >>> generate_unique_filename("profile/+=>/.jpg")
        >>> 'b4959f81-1de0-46a4-bf78-ffc208e149e3-profile.jpg'
    """
    return secure_filename(generate_unique_id() + "-" + filename)


def generate_unique_slug(title, k=8):
    """
    Generate a unique slug for a given title.

    Example:
    >>> generate_unique_slug("This is the Post Title.")
    >>> 'this-is-the-post-title-n9z4k80c'
    """
    random_str = "".join(random.choices((string.ascii_lowercase + string.digits), k=k))
    return slugify(title + "-" + random_str)


def generate_security_code():
    """
    A Method for generating a random (6 DIGIT)
    number for One Time Password(OTP).
    """
    return str(random.randint(100000, 999999))


def generate_unique_id():
    """
    Generating a Unique ID string using
    uuid.uuid4() method.
    """
    return str(uuid.uuid4())


def imagefile_save(save_path, imagefile, filename):
    """
    Save an image file to the specified file path.
    """
    try:
        # Create the directory if it doesn't exist.
        if os.path.exists(save_path):
            os.makedirs(os.path.join(save_path), exist_ok=True)

        # Save the image file.
        imagefile.save(os.path.join(save_path, filename))

        # Log the success info message.
        logging.info("Imagefile saved successfully at: %s" % save_path)
    except OSError as err:
        # Log the error message.
        logging.error("Error while saving file at '%s': %s" % (save_path, err))
        return None


def remove_existing_file(file_path):
    """
    Remove an existing file at the specified path.
    """
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)  # remove the specific file from the directory.
            logging.info("Imagefile removed successfully: %s" % file_path)
    except OSError as err:
        logging.error("Error while removing Imagefile at '%s': %s" % (file_path, err))
