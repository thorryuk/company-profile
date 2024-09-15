from flask import render_template
from . import main_bp

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
