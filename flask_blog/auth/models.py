from datetime import datetime
from itsdangerous import (
        BadSignature,
        SignatureExpired,
        URLSafeTimedSerializer
    )
from sqlalchemy import event
from sqlalchemy import UniqueConstraint

from flask_login import UserMixin
from flask_bcrypt import (
        check_password_hash,
        generate_password_hash
    )

from flask_blog.extensions import database as db
from flask_blog.helpers import (
        cover_image_save,
        post_thumbnail_save,
        profile_image_save
    )
from flask_blog.utils import (
        generate_unique_id,
        generate_security_code
    )


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


class Users(BaseModel, UserMixin):
    """
    A Users model representing user information and authentication.
    * Required Username, Email and Password fields.
    """
    __tablename__ = 'users'

    # A basic info. for 'User' authentication.
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    # 'User' account activation and superuser
    active = db.Column(db.Boolean, default=False, nullable=False)
    superuser = db.Column(db.Boolean, default=False, nullable=False)
    token = db.Column(db.Boolean, default=True, nullable=False)
    security_code = db.Column(db.String(6), default=generate_security_code, nullable=False)

    # Defining 'relationships' with other database model instance.
    profile = db.Relationship('Profile', backref='user', cascade="save-update, merge, delete", lazy=True)
    notifications = db.Relationship('Notification', backref='user', cascade="save-update, merge, delete", lazy=True)
    blogposts = db.Relationship('Blogpost', backref='user', cascade="save-update, merge, delete", lazy=True)
    comments = db.Relationship('Comment', backref='user', cascade="save-update, merge, delete", lazy=True)
    replies = db.Relationship('Reply', backref='user', cascade="save-update, merge, delete", lazy=True)
    likes = db.Relationship('Likepost', backref='user', cascade="save-update, merge, delete", lazy=True)
    saves = db.Relationship('Savepost', backref='user', cascade="save-update, merge, delete", lazy=True)
    followers = db.Relationship('Followers', foreign_keys='Followers.following_id', backref='following', lazy=True)
    following = db.Relationship('Followers', 
                    foreign_keys='Followers.follower_id', backref='follower', 
                    cascade="save-update, merge, delete", lazy=True
                )

    @classmethod
    def get_user_by_username(cls, username):
        """
        Return a User object if the username matches, otherwise return None.
        """
        if not username:
            return None
        return cls.query.filter_by(username=username).first()
    
    @classmethod
    def get_user_by_email(cls, email):
        """
        Return a User object if the email matches, otherwise return None.
        """
        if not email:
            return None
        return cls.query.filter_by(email=email).first()

    def get_profile(self):
        """
        Retrieve the User's profile.
        """
        return Profile.query.filter_by(user_id=self.id).first_or_404()

    def set_username(self, new_username):
        """
        Set or update the username of the User.
        """
        self.username = new_username

    def set_email(self, new_email):
        """
        Set or update the email address of the User. 
        """
        self.email = new_email

    def set_password(self, new_password):
        """
        Set or update the user's password by generating a hashed password.
        """
        self.password = generate_password_hash(new_password)

    def check_password(self, password):
        """
        Check if the provided password matches the User's password.
        Otherwise return False.
        """
        return check_password_hash(self.password, password)

    def generate_token(self, salt=None):
        """
        Generate a token for the user, used for various purposes like.
        # Account verification
        # Reset Password 
        # Reset Email Address
        """
        import config

        serializer = URLSafeTimedSerializer(config.SECRET_KEY)
        token = serializer.dumps({"user_id": self.id}, salt=salt)
        self.token = False
        db.session.commit()
        return token

    @staticmethod
    def verify_token(token, salt=None, max_age=1800):
        """
        Verify if a token is valid and retrieve the associated user.
        Otherwise return 'None'.
        """
        import config

        serializer = URLSafeTimedSerializer(config.SECRET_KEY)
        try:
            user_id = serializer.loads(token, salt=salt, max_age=max_age)["user_id"]
        except (SignatureExpired, BadSignature):
            return None
        return Users.query.get_or_404(user_id)

    def is_active(self):
        """
        Check if the user's account is active. Otherwise return False.
        """
        return self.active

    def is_admin(self):
        """
        Check if the user is a superuser/admin. Otherwise return False.
        """
        return self.superuser

    def is_expired(self):
        """
        Check if the user's token has expired. Otherwise return True.
        """
        return self.token

    def __repr__(self):
        return "User >> {}".format(self.username)


class SocialMixin:
    """
    A class provides a some social link's field 
    for User's Profile instance.
    """

    # 'user' social information
    website_url = db.Column(db.String(150), default="")
    github_url = db.Column(db.String(150), default="")
    twitter_url = db.Column(db.String(150), default="")
    instagram_url = db.Column(db.String(150), default="")
    facebook_url = db.Column(db.String(150), default="")


class Profile(BaseModel, SocialMixin):
    """
    A User Profile Model class related to the 'User' Model instance.
    """
    __tablename__ = 'profile'

    # 'user' basic information
    fullname = db.Column(db.String(50), default="")
    mobile = db.Column(db.String(10), default="")
    gender = db.Column(db.String(10), default="")
    biodata = db.Column(db.String(200), default="")
    address = db.Column(db.String(100), default="")

    # 'user' professional information
    work = db.Column(db.String(100), default="")
    education = db.Column(db.String(100), default="")
    role = db.Column(db.String(100), default="")

    # URL route for 'user' profile image and cover image.
    profile_url = db.Column(db.String(300), default="")
    cover_url = db.Column(db.String(300), default="")

    user_id = db.Column(
        db.String(38), db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False
    )
    
    def set_profile_image(self, filename):
        """
        Set or update the profile image URL.
        """
        return profile_image_save(self, filename)

    def set_cover_image(self, filename):
        """
        Set or update the cover image URL.
        """
        return cover_image_save(self, filename)

    def __repr__(self):
        return "Profile >> {}".format(self.user.username)

# @event.listens_for(Users, "after_insert")
# def create_profile_for_user(mapper, connection, target):
#     """
#     Automatically create and save a profile for a newly inserted user.
#     """
#     assert target.id is not None
#     profile = Profile(user_id=target.id)
#     db.session.add(profile)
#     db.session.commit()


class Followers(BaseModel):
    """
    A Followers model class to represent followers/following relationship.
    """
    __tablename__ = 'followers'

    follower_id = db.Column(db.String(38), db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    following_id = db.Column(db.String(38), db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)

    __table_args__ = (
        UniqueConstraint('follower_id', 'following_id'),
    )
    
    @classmethod
    def follow(cls, follower, following):
        """
        Method to create a follower/following relationship.
        """
        relationship = cls(follower_id=follower.id, following_id=following.id)
        relationship.save()

    @classmethod
    def unfollow(cls, follower, following):
        """
        Method to remove a follower/following relationship.
        """
        relationship = cls.query.filter_by(follower_id=follower.id, following_id=following.id).first()
        if relationship:
            relationship.delete()

    @classmethod
    def get_followers(cls, user):
        """
        Method to get the followers of a user.
        """
        return cls.query.filter_by(following_id=user.id).all()

    @classmethod
    def get_following(cls, user):
        """
        Method to get the users a user is following.
        """
        return cls.query.filter_by(follower_id=user.id).all()

    def __repr__(self):
        return "{} follow {}".format(self.follower_id, self.following_id)

