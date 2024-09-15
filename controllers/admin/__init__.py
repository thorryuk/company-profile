from flask import Blueprint

admin_bp = Blueprint('admin', __name__)

from .dashboard_controller import dashboard_bp
from .master_data_controller import master_data_bp

# Register the admin sub-controllers
admin_bp.register_blueprint(dashboard_bp, url_prefix='/dashboard')
admin_bp.register_blueprint(master_data_bp, url_prefix='/master_data')
