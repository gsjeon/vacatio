from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
 
from vacatio import config
from vacatio import models
 
from vacatio.views.main_views import bp as main_bp
from vacatio.views.test_views import bp as test_bp
 
db = SQLAlchemy()
migrate = Migrate()
 
 
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
 
    with app.app_context():
        db.init_app(app)
        migrate.init_app(app, db)
 
        app.register_blueprint(main_bp)
        app.register_blueprint(test_bp)
 
    return app
