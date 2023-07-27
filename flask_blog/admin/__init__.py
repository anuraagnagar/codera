from flask import Blueprint

from .views import (
    AdminLoginView,
    AdminHomeView,
    AdminLogoutView,
    AdminChangePasswordView,
    ShowUserView,
    AddUserView,
    EditUserView,
    DeleteUserView,
)


admin_login = AdminLoginView.as_view('login')
admin_home = AdminHomeView.as_view('index')
admin_logout = AdminLogoutView.as_view('logout')
admin_change_password = AdminChangePasswordView.as_view('change_password')
admin_show_user = ShowUserView.as_view('show_users')
admin_add_user = AddUserView.as_view('add_user')
admin_edit_user = EditUserView.as_view('edit_user')
admin_delete_user = DeleteUserView.as_view('delete_user')