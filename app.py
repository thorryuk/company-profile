from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__, template_folder='views/templates', static_folder='views/static', static_url_path='/static')
app.config.from_object('config.Config')

# Initialize extensions
# db = SQLAlchemy(app)
# login_manager = LoginManager(app)
# login_manager.login_view = 'auth.login'

# Register Blueprints (controllers)
from controllers.auth import auth_bp
from controllers.admin import admin_bp
from controllers.main import main_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True)