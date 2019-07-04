from flask import render_template, request, Blueprint
from WhatsUp.models import Contact

contacts = Blueprint('contacts', __name__)
