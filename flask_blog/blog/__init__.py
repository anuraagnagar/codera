from flask_blog.auth import LoginForm
from .forms import (
        CreatePostForm,
        EditPostForm,
        PostCommentForm
    )
from .models import (
        Comment,
        Blogpost,
        Likepost,
        Reply,
        Savepost
    )
from .views import (
        BlogpostView,
        CreatePostView,
        DeleteCommentView,
        DeletePostView,
        EditPostView,
        LikePostView,
        SavedPostView
    )

__all__ = [
    "LoginForm",
    "CreatePostForm",
    "EditPostForm",
    "PostCommentForm",
    "Comment",
    "Blogpost",
    "Likepost",
    "Reply",
    "Savepost",
    "BlogpostView",
    "CreatePostView",
    "DeleteCommentView",
    "DeletePostView",
    "EditPostView",
    "LikePostView",
    "SavedPostView"
]


blogpost = BlogpostView.as_view('blogpost', Blogpost, template="blog/blogpost.html")
create_post = CreatePostView.as_view('create_post', Blogpost, template="blog/addpost.html")
edit_post = EditPostView.as_view('edit_post', Blogpost, template="blog/editpost.html")
delete_comment = DeleteCommentView.as_view('delete_comment', Comment)
delete_post = DeletePostView.as_view('delete_post', Blogpost)
like_post = LikePostView.as_view('like_post')
save_post = SavedPostView.as_view('save_post', Savepost, template="blog/saved.html")