from flask import render_template, Blueprint
from flask_login import login_required

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
# @login_required
def index():
    return render_template('/admin/index.html')
