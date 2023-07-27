from flask_blog.auth import Users
from flask_blog.blog import Blogpost
from .models import (
        Contact,
        Notification,
    )
from .forms import ContactForm
from .views import (
        AboutView,
        ContactView,
        DashboardView,
        HomeView,
        NotificationView,
        SearchBlogpostView
    )

__all__ = [
    "Users",
    "Blogpost",
    "Contact",
    "Notification",
    "AboutView",
    "ContactView",
    "DashboardView",
    "HomeView",
    "NotificationView",
    "SearchBlogpostView",
]


about = AboutView.as_view('about', template="app/about.html")
contact = ContactView.as_view('contact', Contact, template="app/contact.html")
dashboard = DashboardView.as_view('dashboard', Users, template="app/dashboard.html")
index = HomeView.as_view('index', Blogpost, template="app/index.html")
notication = NotificationView.as_view('notification', Notification, template="app/notification.html")
search_post = SearchBlogpostView.as_view('search_post', Blogpost, template="app/search.html")
