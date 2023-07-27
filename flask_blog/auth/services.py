from flask import flash, redirect, url_for
from flask_blog.services import send_mail
import config


def send_confirmation(user=None):
    """
    Send an OTP email to the user's email address 
    for account verification.
    """
    if not user or not user.email:
        flash("Invalid user or email address.", category='error')
        return redirect(url_for('app.index'))

    token = user.generate_token('account_verify_token')
    subject = "Received OTP For Account Verification!"
    template = f"""
    Your One Time Password(OTP) is {user.security_code},

    To confirm your {config.SITE_TITLE} Account, please click the link below.
    {url_for('auth.verify_account', token=token)}
    
    This link will use one time only and expire after 30 minutes.
    """
    
    send_mail(email=user.email, subject=subject, context=template)
    flash("Check your mail to verify your account, We have sent an OTP.", category='success')
    return redirect(url_for('auth.verify_account', token=token))


def send_reset_password(user=None):
    """
    A method for send an email to the user's registered 
    email address for reset password.
    """
    try:
        if not user or not user.email:
            flash("Invalid user or email address.", category='error')
            return redirect(url_for('auth.forgot_password'))

        token = user.generate_token('reset_password_token')
        subject = "Request for Reset Password"
        template = f"""
        Hello, {user.username}

        We have received a request to Reset Your '{config.SITE_TITLE}' Password.
        If you didn't make this request, please ignore.

        To reset your password, Please click the link below.
        {url_for('auth.reset_password', token=token)}
        
        This link will use one time only and expire after 30 minutes.
        """
        
        send_mail(email=user.email, subject=subject, context=template)
        flash("A reset password email has been sent.", category='success')
        return redirect(url_for('auth.login'))
    except Exception as e:
        flash("Something went wrong with the backend server.", category='error')
        return redirect(url_for('auth.forgot_password'))


def send_reset_email(email, user=None):
    """
    A method for send an email for resetting the User's email.
    """
    try:
        if not user or not user.email:
            flash("Invalid user or email address.", category='error')
            return redirect(url_for('auth.update_email'))

        token = user.generate_token(salt='reset_email_token')
        subject = "Request for Updating Email Address"
        template = f"""
        Hi, {user.username}

        We have received a request for changing email address.

        To change your email address, Please click the link below.
        { url_for("auth.confirm_email", email=email, token=token) }
        
        This link will use only one time and expire after 30 minutes.
        """
        send_mail(email=email, subject=subject, context=template)
        flash("A reset email link has been sent. Please check your mail.", category='success')
        return redirect(url_for('app.index'))
    except Exception as e:
        flash("Something went wrong with the backend server.", category='error')
        return redirect(url_for('auth.update_email'))

