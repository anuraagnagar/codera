import os
import re
import json
from sqlalchemy import func

from flask import render_template as render
from flask import abort, flash, jsonify, redirect, request, url_for, views

from flask_login import (
        current_user,
        login_required as LoginRequired
    )

from flask_blog.auth import LoginForm
from flask_blog.blog import (
        Blogpost,
        Comment,
        CreatePostForm,
        EditPostForm,
        Likepost,
        PostCommentForm,
        Reply,
        Savepost
    )
from flask_blog.extensions import database as db
from flask_blog.helpers import (
        post_category,
        remove_existing_file
    )

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


class BlogpostView(BaseView):

    def get_context_data(self, post, form):
        author_posts = [posts for posts in Blogpost.query.filter_by(user_id=post.user.id).order_by(Blogpost.created.desc()).all() if posts != post]
        post_likes = [like.user for like in Likepost.query.filter_by(post_id=post.id).all()]
        post_saves = [save.user for save in Savepost.query.filter_by(post_id=post.id).all()]
        post_comments = Comment.query.filter_by(post_id=post.id).order_by(Comment.created.desc()).all()

        context = {
                "params": params,
                "post": post,
                "form": form,
                "login_form": LoginForm(),
                "post_likes": post_likes,
                "post_saves": post_saves,
                "comments": post_comments,
                "author_posts": author_posts
            }
        return context

    def dispatch_request(self, slug=None):
        form = PostCommentForm()
        post = self.model.query.filter(self.model.slug.ilike('%' + slug + '%')).first_or_404()

        if current_user.is_authenticated and form.validate_on_submit():
            content = form.data.get('content', None)
            
            if not content or not len(content) <= 500:
                flash("Your comment should not exceed 500 letters.", category='error')
            else:
                try:
                    comment = Comment(
                        content=content, user_id=current_user.id, post_id=post.id
                    )
                    comment.save()
                    flash("Your comment added successfully.", category='success')
                    return redirect(url_for('blog.blogpost', slug=post.slug)+'#comments')
                except Exception as e:
                    flash("Something went wrong with the backend server.", category='error')
                    return redirect(url_for('blog.blogpost', slug=post.slug))

            return redirect(url_for('blog.blogpost', slug=post.slug))

        context = self.get_context_data(post=post, form=form)
        return render(self.template, **context)


class SavedPostView(views.MethodView):

    decorators = [LoginRequired]

    def __init__(self, model, template):
        self.model = model
        self.template = template

    def get_context_data(self):
        save_posts = self.model.query.filter_by(user_id=current_user.id).order_by(Savepost.created.desc()).all()
        context = {
            "params": params,
            "save_posts": save_posts
        }
        return context
    
    def get(self):
        if current_user.is_authenticated:
            context = self.get_context_data()
            return render(self.template, **context)

    def post(self):
        post_id = request.json.get('post_id')
        post = Blogpost.query.filter_by(id=post_id).first()

        if not post:
            return jsonify({
                "error": "Post not found."
            })

        save_post = self.model.query.filter_by(user_id=current_user.id, post_id=post.id).first()
        if not save_post:
            try:
                post_save = Savepost(user_id=current_user.id, post_id=post.id)
                post_save.save()
                return jsonify({
                    "status": post_save.status,
                    "saves": len(post.saves)
                })
            except Exception as e:
                return jsonify({"error": "Something went wrong."})
        else:
            try:
                db.session.delete(save_post)
                db.session.commit()
                return jsonify({
                    "status": "unsave",
                    "saves": len(post.saves)
                })
            except Exception as e:
                return jsonify({"error": "Something went wrong."})


class LikePostView(views.MethodView):

    decorators = [LoginRequired]
    model = Blogpost

    def post(self, id=None):
        post = self.model.query.filter_by(id=id).first()

        if not post:
            return jsonify({
                "error": "Post not found."
            })

        user_like = Likepost.query.filter_by(user_id=current_user.id, post_id=post.id).first()
        if not user_like:
            try:
                like = Likepost(user_id=current_user.id, post_id=post.id)
                like.save()
                return jsonify({
                    "status": like.status,
                    "likes": len(post.likes)
                })
            except Exception as e:
                return jsonify({"error": "Something went wrong."})
        else:
            try:
                db.session.delete(user_like)
                db.session.commit()
                return jsonify({
                    "status": "unlike",
                    "likes": len(post.likes)
                })
            except Exception as e:
                return jsonify({"error": "Something went wrong."})


class CreatePostView(BaseView):

    decorators = [LoginRequired]
    API_KEY = os.environ.get("TINYMCE_API_KEY", None)

    def handle_request(self, form=None):
        category = form.data.get('category', None)
        title = form.data.get('title', None)
        subtitle = form.data.get('subtitle', None)
        content = form.data.get('content', None)
        imagefile = form.data.get('image_file', None)

        if not category or not title or not subtitle or not content:
            flash("Please fill out the form.", category='error')
        elif category not in post_category():
            flash("Please select a given category for post.", category='error')
        elif not imagefile.filename:
            flash("Add cover image for your post", category='error')
        elif not len(imagefile.filename) <= 250:
            flash("Cover image name length is too long.", category='error')
        elif title in [post.title for post in self.model.query.all()]:
            flash("Title is already exists, Please choose another.", category='error')
        elif len(title) > 100:
            flash("Title does not 'exceed' 100 characters.", category='error')
        elif len(subtitle) > 150:
            flash("Subtitle does not 'exceed' 150 characters.", category='error')
        else:
            try:
                post = self.model(
                        category=category, title=title,
                        subtitle=subtitle, content=content,
                        user_id=current_user.id
                    )
                post.make_slug(title)
                post.set_thumbnail(imagefile)
                post.save()
                flash("Post created successfully.", category='success')
                return redirect(url_for("blog.blogpost", slug=post.slug))
            except Exception as e:
                flash("Something went wrong with the backend server.", category='error')
                return redirect(url_for('blog.create_post'))

        return redirect(url_for('blog.create_post'))

    def dispatch_request(self):
        form = CreatePostForm()

        if form.validate_on_submit():
            return self.handle_request(form=form)

        return render(self.template, params=params, form=form, tiny_api_key=self.API_KEY)


class EditPostView(BaseView):

    API_KEY = os.environ.get("TINYMCE_API_KEY", None)

    def get_context_data(self, post=None, form=None):
        context = {
                "params": params,
                "post": post,
                "form": form,
                "tiny_api_key": self.API_KEY
            }
        return render(self.template, **context)

    def handle_request(self, post=None):
        form = EditPostForm()
        print(post.get_filename())
        if form.validate_on_submit():
            print(form.data)

            category = form.data.get('category', None)
            title = form.data.get('title', None)
            subtitle = form.data.get('subtitle', None)
            content = form.data.get('content', None)
            imagefile = form.data.get('image_file', None)

            if not category or not title or not subtitle or not content:
                flash("Please fill out the form.", category='error')
            elif category not in post_category():
                flash("Please select a given category for post.", category='error')
            elif not len(imagefile.filename) <= 250:
                flash("Cover image name length is too long.", category='error')
            elif title in [_post.title for _post in self.model.query.all() if _post != post]:
                flash("Title is already exists, Please choose another.", category='error')
            elif len(title) > 100:
                flash("Title does not 'exceed' 100 characters.", category='error')
            elif len(subtitle) > 150:
                flash("Subtitle does not 'exceed' 150 characters.", category='error')
            else:
                try:
                    post.category = category
                    post.title = title
                    post.subtitle = subtitle
                    post.content = content
                    post.make_slug(title)
                    post.set_thumbnail(imagefile)
                    db.session.commit()
                    flash("Your post edit successfully.", category='success')
                    return redirect(url_for('blog.blogpost', slug=post.slug))
                except Exception as e:
                    flash("Something went wrong with backend server.", category='error')
                    return redirect(url_for('blog.edit_post', slug=slug))
            
            return redirect(url_for('blog.edit_post', slug=slug))

        return self.get_context_data(post=post, form=form)

    def dispatch_request(self, slug=None):
        post = self.model.query.filter_by(slug=slug).first_or_404()
        
        if current_user.is_authenticated and post.user == current_user:
            return self.handle_request(post=post)

        return abort(404)

class DeletePostView(BaseView):

    def dispatch_request(self, slug=None):

        if current_user.is_authenticated:
            post = self.model.query.filter_by(slug=slug).first_or_404()

            if post.user == current_user:
                try:
                    import config

                    file_path = os.path.join(config.UPLOAD_FOLDER, "thumbnail", post.filename)
                    remove_existing_file(file_path=file_path)
                    db.session.delete(post)
                    db.session.commit()
                    flash("Your post was deleted.", category='success')
                    return redirect(url_for('app.index'))
                except Exception as e:
                    flash("Something went wrong with the backend server.", category='error')
                    return redirect(url_for('blog.blogpost', slug=slug))

        return abort(404)


class DeleteCommentView(BaseView):

    def dispatch_request(self, id=None):

        if current_user.is_authenticated:
            comment = self.model.query.filter_by(id=id).first_or_404()

            post = Blogpost.query.filter_by(id=comment.post.id).first_or_404()

            if (comment.user == current_user) or (post.user == current_user):
                try:
                    db.session.delete(comment)
                    db.session.commit()
                    flash("Your comment deleted successfully.", category='success')
                    return redirect(url_for('blog.blogpost', slug=post.slug))
                except Exception as e:
                    flash("Something went wrong with the backend server.", category='error')
                    return redirect(url_for('app.index'))

        return abort(404)
    