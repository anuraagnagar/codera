import re
import json
from sqlalchemy import func

from flask import render_template as render
from flask import abort, flash, jsonify, redirect, request, url_for, views
from flask_login import (
        current_user,
        login_required as LoginRequired
    )

from flask_blog.blog import Blogpost
from flask_blog.app import ContactForm
from .services import send_contact_mail

with open("flask_blog/confi.json", "r") as c:
    params = json.load(c)["parameter"]


class BaseView(views.View):
    """
    A Base view class providing common functionality for
    all subclasses.
    """

    init_every_request = False

    def __init__(self, model=None, template=None):
        """
        Initializes the BaseView with the provided 
        model and template common.
        """
        self.model = model
        self.template = template


class HomeView(BaseView):
    """
    A View class for handling the home page.

    This class extends the `BaseView` and provides functionality 
    for rendering the home page template and fetching data
    to be displayed on the page.
    """
    POSTS_PER_PAGE = 20
    CATEGORY_POSTS_PER_PAGE = 3

    def get_all_posts(self, page):
        """
        Retrieve all blog posts to be displayed on the home page.
        """
        posts =  self.model.query \
            .order_by(self.model.created.desc()) \
            .paginate(page=page, per_page=self.POSTS_PER_PAGE)
        
        return posts

    def get_category_posts(self, category, page):
        """
        Retrieve blog posts by category and displayed on the home page.
        """
        category = self.model.query \
            .filter_by(category=category) \
            .order_by(self.model.created.desc()) \
            .paginate(page=page, per_page=self.CATEGORY_POSTS_PER_PAGE)
        
        return category

    def get_context_data(self, page=1):
        context = {
            "params": params,
            "posts": self.get_all_posts(page),
            "category": self.get_category_posts('programming', page)
        }
        return context
    
    def dispatch_request(self):
        """
        A method for handling the request and render 
        the template with the provided context data.
        """
        context = self.get_context_data()
        return render(self.template, **context)


class ContactView(BaseView):
    """
    A View class handling request for contact page
    Supports GET and POST methods. 
    """

    def handle_request(self, form=None):
        name = form.data.get('name', None)
        email = form.data.get('email', None)
        mobile = form.data.get('mobile', None)
        message = form.data.get('message', None)

        if not name or not email or not mobile or not message:  
            flash("Please fill out the form.", category='error')
        elif not re.match(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", email):
            flash("Invalid email address.", category='error')
        elif not re.match(r"^[0-9]*$", mobile):
            flash("Phone number is invalid.", category='error')
        else:
            try:
                contact = self.model(name=name, email=email, mobile=mobile, message=message)
                contact.save()
                send_contact_mail(name, email, message)
                flash("Thank you for contacting.", category='success')
                return redirect(url_for('app.index'))
            except Exception as e:
                flash("Something went wrong with the backend server.", category='error')
                return redirect(url_for('app.contact'))

        return redirect(url_for('app.contact'))

    def dispatch_request(self):
        """
        A method for handling GET and POST requests 
        for save contact information.
        """
        form = ContactForm()

        if form.validate_on_submit():
            return self.handle_request(form=form)

        return render(self.template, params=params, form=form)


class AboutView(BaseView):
    """
    A View class handling request for about page.
    Supports GET methods only.
    """

    def dispatch_request(self):
        """
        A method only handling GET requests 
        for About page.
        """
        return render(self.template, params=params)


class SearchBlogpostView(BaseView):
    """
    A View class handling request for searching blogpost.
    Supports GET methods only.
    """

    def dispatch_request(self):
        """
        A method only handling GET requests 
        for Search page.
        """
        query = request.args.get('query')
        match_query = self.model.title.ilike('%' + query + '%')
        like_by_desc = func.count(Likepost.id).desc()
        posts = self.model.query.join(self.model.likes).filter(match_query).group_by(self.model.id).filter(Blogpost.likes.any()).order_by(like_by_desc).all()
        return render(
            self.template, params=params, posts=posts, query=query
        )


class NotificationView(BaseView):

    decorators = [LoginRequired]

    def dispatch_request(self):
        return render(self.template, params=params)


class DashboardView(BaseView):

    def dispatch_request(self, page=1, username=None):

        user = self.model.query.filter_by(username=username).first_or_404()
        
        posts = Blogpost.query.filter_by(user_id=user.id).order_by(Blogpost.created.desc()).all()

        return render(self.template, params=params, user=user, posts=posts)
