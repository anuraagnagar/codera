from datetime import datetime

from flask_blog.extensions import database as db
from flask_blog.utils import generate_unique_id


class TimedStampMixin:
    """
    A Time Stamp Mixin Class for date and time.
    """
    
    created = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated = db.Column(
                db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
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
        

class Contact(BaseModel):
    """
    A Contact Model instance.
    """
    __tablename__ = 'contact'

    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    mobile = db.Column(db.String(10), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return "Contact >> {}".format(self.name)


class Notification(BaseModel):
    """
    A Notification Model class representing User notifications.
    """

    __tablename__ = 'notification'

    # Notification details
    message = db.Column(db.String(200), nullable=False)
    is_read = db.Column(db.Boolean, default=False, nullable=False)

    user_id = db.Column(
        db.String(38), db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False
    )

    def mark_as_read(self):
        """
        Mark the notification as read.
        """
        self.is_read = True
    
    def __repr__(self):
        return "Notification >> {}".format(self.user_id.username)

