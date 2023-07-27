from flask_blog.blueprints import app_blueprint as app
from flask_blog import app as views


methods = ["GET", "POST"]

"""
Url routes define for application main view.
"""

app.add_url_rule(
        "/", 
        view_func=views.index
    )
app.add_url_rule(
        "/contact", 
        view_func=views.contact, 
        methods=methods
    )
app.add_url_rule(
        "/about", 
        view_func=views.about
    )
app.add_url_rule(
        "/search", 
        view_func=views.search_post
    )
app.add_url_rule(
        "/notification", 
        view_func=views.notication
    )
app.add_url_rule(
        "/<string:username>", 
        view_func=views.dashboard
    )

