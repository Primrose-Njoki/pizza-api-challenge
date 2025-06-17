from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    
    from server.controllers.pizza_controller import pizza_bp
    from server.controllers.restaurant_controller import restaurant_bp
    from server.controllers.restaurant_pizza_controller import rp_bp
    
    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_bp)
    app.register_blueprint(rp_bp)
    
    return app