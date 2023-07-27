from sqlalchemy.exc import DatabaseError
from werkzeug.exceptions import (
    BadRequest, MethodNotAllowed, NotFound, Unauthorized
)
from wtforms import Form
from flask import flash, redirect, request, url_for
from flask import render_template as render
from flask_wtf.csrf import CSRFError
import json

with open("flask_blog/confi.json", "r") as c:
    params = json.load(c)["parameter"]


def configure(app=None):
    """
    Configures error handlers for common exceptions 
    in the Flask application.
    """

    def _error_handler(e, message):
        """
        A error handler method that flashes an error message
        and redirects to the index view.
        """
        flash(message, category='error')
        return redirect(request.path or url_for('app.index'))

    @app.errorhandler(BadRequest)
    def bad_request(e):
        """
        Error handler for BadRequest exception.
        """
        return _error_handler(e, "The request was invalid. Please check your input.")

    @app.errorhandler(Unauthorized)
    def unauthorized_error(e):
        """
        A Error handler for Unauthorized exception.
        """
        return _error_handler(e, "You are not authorized to access.")

    @app.errorhandler(NotFound)
    def page_not_found(e, template='error.html'):
        """
        A Error handler for NotFound exception.
        """
        return render(template, params=params), 404

    @app.errorhandler(MethodNotAllowed)
    def method_not_allowed(e):
        """
        A Error handler for MethodNotAllowed exception.
        """
        return _error_handler(e, "This method is not allowed.")

    @app.errorhandler(DatabaseError)
    def database_error(e):
        """
        A Error handler for DatabaseError exception.
        """
        return _error_handler(e, "Something went wrong with the backend server.")

    @app.errorhandler(CSRFError)
    def csrf_error(e):
        """
        A Method error handler for missing CSRF token. 
        """
        return _error_handler(e, "Bad Request CSRF token is missing.")