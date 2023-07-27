from flask import url_for
from werkzeug.utils import secure_filename
from flask_blog.utils import generate_unique_filename
from config import POST_THUMBNAIL_PATH, PROFILE_IMAGE_PATH, COVER_IMAGE_PATH
import uuid
import os


def remove_existing_file(file_path):
    """
    A method for removing an existing image file.
    """
    print(file_path)
    if os.path.isfile(file_path):
        os.remove(file_path)

def imagefile_save(file_path, imagefile, filename):
    """
    Save an image file to the specified file path.
    """
    try:
        # Create the directory if it doesn't exist
        os.makedirs(os.path.join(file_path), exist_ok=True)
        # Save the image file
        imagefile.save(
            os.path.join(file_path, filename)
        )
    except Exception as e:
        return None

def profile_image_save(instance, imagefile=None, save_path="profile"):
    """
    Save the profile image file for the User.
    """
    if not imagefile.filename == "":
        profile_name = generate_unique_filename(imagefile.filename)
        if instance.profile_url != None or "":
            file_path = os.path.join(UPLOAD_FOLDER, save_path, instance.profile_url)
            remove_existing_file(file_path)
        instance.profile_url = profile_name
        imagefile_save(imagefile, save_path, instance.profile_url)
    return None

def cover_image_save(instance, imagefile=None, save_path="cover"):
    """
    Save the cover image file for the User profile.
    """
    if not imagefile.filename == "":
        cover_name = generate_unique_filename(imagefile.filename)
        if instance.cover_url != None or "":
            file_path = os.path.join(UPLOAD_FOLDER, save_path, instance.cover_url)
            remove_existing_file(file_path)
        instance.cover_url = cover_name
        imagefile_save(imagefile, save_path, instance.cover_url)
    return None

def post_thumbnail_save(instance, imagefile, save_path):
    """
    Save the post thumbnail image file for the Blogpost.
    """

    if not imagefile.filename == "":
        filename = generate_unique_filename(imagefile.filename)
        if instance.filename != None or "":
            file_path = os.path.join(POST_THUMBNAIL_PATH, instance.get_filename())
            remove_existing_file(file_path)
        instance.filename = str(os.path.join('assets', 'uploads', save_path, filename))
        imagefile_save(POST_THUMBNAIL_PATH, imagefile, filename)
    return None

def post_category():
    categories = [
        "programming", "python", "javascript", "web-development"
    ]
    return categories