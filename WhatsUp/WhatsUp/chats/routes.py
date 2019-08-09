from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from WhatsUp import db, bcrypt
from WhatsUp.models import Account, Chat, Contact

chats = Blueprint("chats", __name__)
