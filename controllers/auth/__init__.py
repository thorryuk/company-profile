from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

from .auth_controller import *
