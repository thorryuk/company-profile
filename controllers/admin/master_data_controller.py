from flask import render_template, Blueprint
from flask_login import login_required

master_data_bp = Blueprint('master_data', __name__)

@master_data_bp.route('/')
# @login_required
def master_data():
    return render_template('master_data.html')
