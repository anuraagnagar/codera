from flask_blog import auth as views
from flask_blog.blueprints import auth_blueprint as auth

methods = ["GET", "POST"]

"""
Url define for Auth Module handling 
User Registeration & authentication route.
"""

auth.add_url_rule(
        "/account/create", 
        view_func=views.register, 
        methods=methods
    )
auth.add_url_rule(
        "/account/login", 
        view_func=views.login, 
        methods=methods
    )
auth.add_url_rule(
        "/account/logout", 
        view_func=views.logout
    )
auth.add_url_rule(
        "/account/verify/token?<string:token>", 
        view_func=views.verify_account, 
        methods=methods
    )
auth.add_url_rule(
        "/account/password/forgot", 
        view_func=views.forgot_password, 
        methods=methods
    )
auth.add_url_rule(
        "/account/password/reset/token?<string:token>", 
        view_func=views.reset_password, 
        methods=methods
    )
auth.add_url_rule(
        "/account/setting", 
        view_func=views.account, 
        methods=methods
    )
auth.add_url_rule(
        "/account/setting/password/change", 
        view_func=views.change_password, 
        methods=methods
    )
auth.add_url_rule(
        "/account/setting/email/reset", 
        view_func=views.update_email, 
        methods=methods
    )
auth.add_url_rule(
        "/account/confirm/email?<string:email>/token?<string:token>", 
        view_func=views.confirm_email, 
        methods=methods
    )
auth.add_url_rule(
        "/account/profile/edit", 
        view_func=views.edit_profile, 
        methods=methods
    )