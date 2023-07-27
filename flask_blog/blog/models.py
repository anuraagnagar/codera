from datetime import datetime
from slugify import slugify
from sqlalchemy import UniqueConstraint

from flask_blog.extensions import database as db
from flask_blog.helpers import post_thumbnail_save
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
        

class Blogpost(BaseModel):
    """
    A Blogpost Model instance.
    """
    __tablename__ = 'blogpost'
    
    category = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(150), nullable=False)
    slug = db.Column(db.String(100), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    filename = db.Column(db.String(300), nullable=False)

    user_id = db.Column(
        db.String(38), db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False
    )

    # Defining 'relationships' with other model class.
    comments = db.Relationship('Comment', backref='post', cascade="save-update, merge, delete", lazy=True)
    likes = db.Relationship('Likepost', backref='post', cascade="save-update, merge, delete", lazy=True)
    saves = db.Relationship('Savepost', backref='post', cascade="save-update, merge, delete", lazy=True)

    def make_slug(self, title):
        """
        Generates a slug for the blog post based on the given title.

        # Example:
            post = Blogpost()
            post.make_slug("My Blog Post Title")
            print(blog_post.slug)  # Output: "my-blog-post-title"
        """
        new_slug = slugify(title)
        self.slug = new_slug

    def get_filename(self):
        file_path = str(self.filename).split('\\')
        return file_path[int(len(file_path)-1)]

    def set_thumbnail(self, filename):
        """
        Sets the thumbnail for the blog post.

        # Example:
            post = Blogpost()
            thumbnail_path = post.set_thumbnail("thumbnail.jpg")
            print(thumbnail_path)  # Output: "/thumbnails/thumbnail.jpg"
        """
        return post_thumbnail_save(self, filename, save_path='thumbnail')

    def __repr__(self):
        return "Blogpost >> {}".format(self.title)


class Comment(BaseModel):
    """
    A Model inctance for representing a comments on a blog post.
    """
    __tablename__ = 'comment'

    content = db.Column(db.String(500), nullable=False)

    user_id = db.Column(
        db.String(38), db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False
    )

    post_id = db.Column(
        db.String(38), db.ForeignKey('blogpost.id', ondelete="CASCADE"), nullable=False
    )

    # Defining 'relationship' with other model class.
    replies = db.Relationship('Reply', backref='comment', cascade="save-update, merge, delete", lazy=True)

    def __repr__(self):
        return "Comment >> {}".format(self.user.username)


class Reply(BaseModel):
    """
    A Model inctance for representing a reply on a blog post comments.
    """

    __tablename__ = 'reply'

    content = db.Column(db.String(400), nullable=False)

    user_id = db.Column(
        db.String(38), db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False
    )

    comment_id = db.Column(
        db.String(38), db.ForeignKey('comment.id', ondelete="CASCADE"), nullable=False
    )

    def __repr__(self):
        return "Reply >> {}".format(self.user.username)


class Likepost(BaseModel):
    """
    A Model inctance for representing a like on a blog post.
    """

    __tablename__ = 'likepost'
      
    status = db.Column(db.String(10), default="like", nullable=False)

    user_id = db.Column(
        db.String(38), db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False
    )

    post_id = db.Column(
        db.String(38), db.ForeignKey('blogpost.id', ondelete="CASCADE"), nullable=False
    )

    __table_args__ = (
        UniqueConstraint('user_id', 'post_id'),
    )

    def __repr__(self):
        return "Liked By >> {}".format(self.user.username)


class Savepost(BaseModel):
    """
    A Savepost Model class for saving posts by users.
    """

    __tablename__ = 'savepost'

    status = db.Column(db.String(10), default="save", nullable=False)

    user_id = db.Column(
        db.String(38), db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False
    )

    post_id = db.Column(
        db.String(38), db.ForeignKey('blogpost.id', ondelete="CASCADE"), nullable=False
    )

    __table_args__ = (
        UniqueConstraint('user_id', 'post_id'),
    )

    def __repr__(self):
        return "Savepost >> {}".format(self.user.username)

