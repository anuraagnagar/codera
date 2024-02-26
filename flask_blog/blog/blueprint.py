from flask import Blueprint

"""
Blog Blueprints for our application.

blog_blueprint (Blueprint):
    Blueprint for the blog module.
"""

blog_blueprint = Blueprint("blog", __name__, template_folder="templates")
