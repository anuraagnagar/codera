from flask import Flask as FlaskApp
from flask import abort, flash, redirect, request, url_for


def blog_app(config=None):
    """
    Creates and configures a Flask application for our blog.

    # Args:
        config (object): Important.
        config object to be used for the application configuration.
        
    # Returns:
        Flask: 'app' The Flask application instance after all configurations.
    """
    
    app = FlaskApp(__name__, template_folder="templates")

    from flask_blog import routes
    from flask import render_template
    
    configure_application(app, config)
    configure_extensions(app)
    configure_blueprint(app)
    configure_errorhandlers(app)
    configure_template_filter(app)
    
    @app.get('/new_one')
    def new_route():
        # return abort(404)
        return render_template("app/new.html")

    return app

def configure_application(app=None, config=None):
    
    if not config:
        raise ValueError("Config object is not provided.")

    # Application configuration using from config file.
    app.config.from_object(config)


def configure_extensions(app=None):
    """
    Configure following extensions for the Our Application.
    """
    from .extensions import login_manager
    from .extensions import database
    from .extensions import migration
    from .extensions import tinymce
    from .extensions import admin
    from .extensions import babel
    from .extensions import bycrpt
    from .extensions import csrf
    from .extensions import mail
    
    # initialize required extension for our application.
    login_manager.init_app(app)
    database.init_app(app)
    migration.init_app(app, database, command='db')
    tinymce.init_app(app)
    admin.init_app(app)
    babel.init_app(app)
    bycrpt.init_app(app)
    csrf.init_app(app)
    mail.init_app(app)
    
    config_user_manager(login_manager)
    

def config_user_manager(manager=None):
    """
    Configure the Flask Login User Manager.
    """
    from flask_blog import Users

    @manager.user_loader
    def load_user(id):
        """
        Load a user for login_manager via their ID.
        """
        return Users.query.get_or_404(id)

    @manager.unauthorized_handler
    def unauthoried_route():
        """
        Handling unauthorized routes and redirect 
        to the login page.
        """
        flash("Please log in to access this page.", category='warning')
        return redirect(url_for('auth.login', redirect_url=request.path))


def configure_blueprint(app=None):
    """
    Configure and register the following blueprints 
    for the Flask Blog Application.
    """
    from .blueprints import app_blueprint
    from .blueprints import auth_blueprint
    from .blueprints import blog_blueprint
    from .blueprints import tute_blueprint

    # register application blueprints.
    app.register_blueprint(app_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(blog_blueprint)
    app.register_blueprint(tute_blueprint)


def configure_errorhandlers(app=None):
    """
    Configure custom error handlers for the Our Application.
    """
    from flask_blog import handlers
    handlers.configure(app)


def configure_template_filter(app=None):
    """
    Configure some custom template filters for the Our Application.
    """
    from flask_blog import filters
    filters.configure(app)

