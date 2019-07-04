from flask import render_template, request, Blueprint
from flask_login import current_user
from WhatsUp import cu

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('chats.list'))
    else:
        return redirect(url_for('accounts.login'))

@main.route('/about')
def about():
    return render_template('about.html', title='About')
