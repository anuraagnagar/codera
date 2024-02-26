from datetime import datetime

from flask_blog.extensions import database as db


class TimedStampMixin:
    """
    A Time Stamp Mixin Class for date and time.
    """

    created = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )


class SocialMixin:
    """
    A class provides a some social link's field
    for User's Profile instance.
    """

    # users social information.
    website_url = db.Column(db.String(150), default="")
    github_url = db.Column(db.String(150), default="")
    twitter_url = db.Column(db.String(150), default="")
    linkedin_url = db.Column(db.String(150), default="")
    facebook_url = db.Column(db.String(150), default="")
