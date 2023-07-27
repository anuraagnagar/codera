from datetime import datetime
import timeago


def configure(app=None):
    """
    Configures the Flask application and register the following template filters.
    """

    @app.template_filter('timeago')
    def time_ago(date):
        """
        Returns the relative time ago formatted string for the given date.
        """
        return timeago.format(date, now=datetime.now())

    @app.template_filter('date')
    def date(timestamp):
        """
        Returns the date formatted string for the given timestamp.
        """
        return timestamp.strftime('%d %B %Y')

    @app.template_filter('time')
    def time(timestamp):
        """
        Returns the time formatted string for the given timestamp.
        """
        return timestamp.strftime('%I:%M %p')