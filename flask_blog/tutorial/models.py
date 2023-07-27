from datetime import datetime
from sqlalchemy import event
from sqlalchemy import UniqueConstraint
from slugify import slugify

from flask_blog.extensions import database as db
from flask_blog.utils import generate_unique_id


class TimedStampMixin:
    """
    A Time Stamp Mixin Class for date and time.
    """
    
    created = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated = db.Column(
                db.DateTime, default=datetime.now,
                onupdate=datetime.now, nullable=False
            )


class BaseModel(db.Model, TimedStampMixin):
    """
    A Base Model Class for all model instance.
    """

    __abstract__ = True

    id = db.Column(
            db.String(38), 
            primary_key=True, 
            unique=True,
            default=generate_unique_id, 
            nullable=False
        )

    def save(self):
        """
        Saves the information to the database.
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        Deletes the information from the database.
        """
        db.session.delete(self)
        db.session.commit()

    
class Tutorials(BaseModel):
    """
    A Tutorial Model class for app tutorials.
    """

    __tablename__ = 'tutorials'

    title = db.Column(db.String(50), nullable=False)
    slug = db.Column(db.String(50), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    published = db.Column(db.Boolean, default=False, nullable=False)
    published_date = db.Column(db.DateTime, nullable=True)
    views = db.Column(db.Integer, default=0, nullable=False)

    author_id = db.Column(
        db.String(38), db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False
    )

    # Relationship with the author
    author = db.Relationship('Users', backref='tutorials', cascade="save-update, merge, delete")

    def __repr__(self):
        return "Tutorial >> {}".format(self.title)

    def make_slug(self):
        """
        Generate a slug based on the tutorial title.
        """
        self.slug = slugify(self.title)

    def publish(self):
        """
        Set the tutorial as published and update the published date.
        """
        self.published = True
        self.published_date = datetime.now()

