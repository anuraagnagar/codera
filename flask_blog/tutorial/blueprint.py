from flask import Blueprint


"""
Tutorial Blueprint for our application.

tute_blueprint (Blueprint):
    Blueprint for the tutorial module.
"""


tute_blueprint = Blueprint("tute", __name__, template_folder="templates")