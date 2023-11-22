from flask_blog.application import blog_app as Codera

from flask_blog.auth import Users
from flask_blog.auth import Profile
from flask_blog.auth import Followers
from flask_blog.app import Contact
from flask_blog.app import Notification
from flask_blog.blog import Blogpost
from flask_blog.blog import Comment
from flask_blog.blog import Likepost
from flask_blog.blog import Savepost
from flask_blog.blog import Reply
from flask_blog.tutorial import Tutorials

from flask_blog.app import ContactForm
from flask_blog.auth import RegisterForm
from flask_blog.auth import LoginForm
from flask_blog.auth import AccountVerifyForm
from flask_blog.auth import ForgotPasswordForm
from flask_blog.auth import ResetPasswordForm
from flask_blog.auth import ResetEmailForm
from flask_blog.auth import ChangePasswordForm
from flask_blog.auth import EditProfileForm
from flask_blog.auth import DeleteAccountForm
from flask_blog.blog import CreatePostForm
from flask_blog.blog import PostCommentForm


__all__ = [
    # main application
    "Codera",

    # database models
    "Users",
    "Profile",
    "Followers",
    "Notification",
    "Blogpost",
    "Likepost",
    "Savepost",
    "Comment",
    "Reply",
    "Contact",
    "Tutorials",

    # flask WTF forms
    "RegisterForm",
    "LoginForm",
    "AccountVerifyForm",
    "ForgotPasswordForm",
    "ResetPasswordForm",
    "ResetEmailForm",
    "ChangePasswordForm",
    "DeleteAccountForm",
    "ContactForm",
    "EditProfileForm",
    "CreatePostForm",
    "PostCommentForm",

]
