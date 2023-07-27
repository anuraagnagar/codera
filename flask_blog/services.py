from flask_mail import Message
from flask_blog.extensions import mail


def send_mail(email, subject, context):
    """
    Sends an email to the specified email address.

    # Args:
        email (str): The recipient's email address.
        subject (str): The subject of the email.
        context (str): The body/content of the email.

    # Example:
        send_mail('example@example.com', 'Hello', 'This is the email body.')
    """
    import config
    
    sender = config.MAIL_USERNAME
    message = Message(
            subject=subject, recipients=[email], sender=sender
        )
    message.body = context
    print(message.body)
    mail.connect()
    mail.send(message)

    