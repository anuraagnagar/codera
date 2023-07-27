from flask import Blueprint

"""
App Blueprint for our application.

app_blueprint (Blueprint):
    Blueprint for the app module.
"""

app_blueprint = Blueprint("app", __name__, template_folder="templates")