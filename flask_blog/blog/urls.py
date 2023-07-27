from flask_blog.blueprints import blog_blueprint as blog
from flask_blog import blog as views

methods = ["GET", "POST"]

"""
Url routes define for application blog related view.
"""

blog.add_url_rule(
        "/like-post/<string:id>", 
        view_func=views.like_post
    )
blog.add_url_rule(
        "/saved/posts", 
        view_func=views.save_post
    )
blog.add_url_rule(
        "/post/<string:slug>", 
        view_func=views.blogpost, 
        methods=methods
    )
blog.add_url_rule(
        "/create/new", 
        view_func=views.create_post, 
        methods=methods
    )
blog.add_url_rule(
        "/post/<string:slug>/edit", 
        view_func=views.edit_post,
        methods=methods
    )
blog.add_url_rule(
        "/post/<string:slug>/delete", 
        view_func=views.delete_post
    )
blog.add_url_rule(
        "/comment/delete/<string:id>", 
        view_func=views.delete_comment
    )