from .models import (
        Users, 
        Followers, 
        Profile,
    )
from .forms import (
        AccountVerifyForm,
        ChangePasswordForm,
        DeleteAccountForm,
        EditProfileForm,
        ForgotPasswordForm,
        LoginForm,
        RegisterForm,
        ResetEmailForm,
        ResetPasswordForm
    )
from .views import (
        AccountView,
        ChangePasswordView,
        ConfirmEmailView,
        ForgetPasswordView,
        GithubLoginView,
        GithubLoginRedirectView,
        GoogleLoginView,
        GoogleLoginRedirectView,
        LoginView,
        LogoutView,
        RegisterView,
        ResetEmailView,
        ResetPasswordView,
        UserDetailView,
        VerifyAccountView,
    )

__all__ = [
    "Users",
    "Followers",
    "Profile",
    "AccountVerifyForm",
    "ChangePasswordForm",
    "DeleteAccountForm",
    "EditProfileForm",
    "ForgotPasswordForm",
    "LoginForm",
    "RegisterForm",
    "ResetEmailForm",
    "ResetPasswordForm"
    "AccountView",
    "ChangePasswordView",
    "ConfirmEmailView",
    "ForgetPasswordView",
    "GithubLoginView",
    "GithubLoginRedirectView",
    "GoogleLoginView",
    "GoogleLoginRedirectView",
    "LoginView",
    "LogoutView",
    "RegisterView",
    "ResetEmailView",
    "ResetPasswordView",
    "UserDetailView",
    "VerifyAccountView",
]


account = AccountView.as_view('settings', Users, template="auth/settings.html")
change_password = ChangePasswordView.as_view('change_password', Users, template="auth/changepassword.html")
confirm_email = ConfirmEmailView.as_view('confirm_email', Users, template="auth/confirmemail.html")
edit_profile = UserDetailView.as_view('edit_profile', Users, template="auth/profile.html")
forgot_password = ForgetPasswordView.as_view('forgot_password', Users, template="auth/forgotpassword.html")
login = LoginView.as_view('login', Users, template="auth/login.html")
logout = LogoutView.as_view('logout')
register = RegisterView.as_view('register', Users, template="auth/register.html")
reset_password = ResetPasswordView.as_view('reset_password', Users, template="auth/resetpassword.html")
update_email = ResetEmailView.as_view('update_email', Users, template="auth/resetemail.html")
verify_account = VerifyAccountView.as_view('verify_account', Users, template="auth/verify.html")