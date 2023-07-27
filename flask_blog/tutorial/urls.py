from flask_blog import tutorial as views
from flask_blog.blueprints import tute_blueprint as tute

"""
Url routes for Tutorial related pages.
"""

tute.add_url_rule(
        "/tutorial/java", 
        view_func=views.java
    )
tute.add_url_rule(
        "/tutorial/javascript", 
        view_func=views.javascript
    )
tute.add_url_rule(
        "/tutorial/python/starting-python", 
        view_func=views.starting_python
    )
tute.add_url_rule(
        "/tutorial/python/install-python", 
        view_func=views.install_python
    )
tute.add_url_rule(
        "/tutorial/python/vscode-setup", 
        view_func=views.vscode_setup
    )
tute.add_url_rule(
        "/tutorial/python/first-program", 
        view_func=views.first_program
    )