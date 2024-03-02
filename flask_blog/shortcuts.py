from sqlalchemy.exc import DatabaseError, SQLAlchemyError
from flask import abort


def authenticated_token(user, token=None, salt=None):
    """
    Authenticate the user generated token for URL.
    Verify the token using the Users model verify_token() method.
    Returns the signed data if token valid, otherwise None.
    """
    return user.verify_token(token=token, salt=salt)


def get_auth_user(users, user_id=None):
    """
    Get the authenticated user based on the provided User ID.
    Return the User instance if exists, otherwise None.
    """
    return users.query.get_or_404(user_id)


def get_object_or_404(klass, **kwargs):
    """
    Get the object that matches the given query parameters
    or raise a 404 error if not found.

    :param model: SQLAlchemy model class
    :param kwargs: Query parameters
    :return: The queried object
    """

    try:
        instance = klass.query.filter_by(**kwargs).first_or_404()
        return instance
    except (DatabaseError, SQLAlchemyError) as err:
        # Return 500 HttpException for internal server error.
        return abort(500)
