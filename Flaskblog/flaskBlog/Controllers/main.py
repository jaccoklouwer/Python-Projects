from flask import render_template, request, Blueprint
from flaskBlog.models import Post

'''
Here are the routes defined for all general pages.
These pages are not related to any model.
'''

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.date_posted.desc()).paginate(per_page=5, page=page)
    return render_template('home.html', posts=posts)


@main.route('/about')
def about():
    return render_template('about.html', title='About')
