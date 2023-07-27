from flask import flash, redirect, url_for
from flask_blog.services import send_mail


def send_contact_mail(name, email, message):
    """
    Send an email when user submitting contact form.
    """
    try:
        subject = f"Message from {name}"
        msg_body = f"{message}"
        send_mail(
            email=email, subject=subject, context=msg_body
        )
    except Exception as e:
        flash("Something went wrong with the backend server.", category='error')
        return redirect(url_for('app.contact'))
