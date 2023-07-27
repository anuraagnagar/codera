from flask import Blueprint

"""
Auth Blueprints for our application.

auth (Blueprint):
    Blueprint for the authentication module.
"""

auth_blueprint = Blueprint("auth", __name__, template_folder="templates")
