from flask_blog import admin as views
from flask_blog.admin import admin_blueprint as admin 

# URL routes for 'User Administration Management'.
admin.add_url_rule("/admin", view_func=views.admin_home)
admin.add_url_rule("/admin/login", view_func=views.admin_login)
admin.add_url_rule("/admin/logout", view_func=views.admin_logout)
admin.add_url_rule("/admin/password/change", view_func=views.admin_change_password)
admin.add_url_rule("/admin/user", view_func=views.admin_show_user)
admin.add_url_rule("/admin/user/add", view_func=views.admin_add_user)
admin.add_url_rule("/admin/user/<string:username>", view_func=views.admin_edit_user)
admin.add_url_rule("/admin/user/<string:username>/delete", view_func=views.admin_delete_user)