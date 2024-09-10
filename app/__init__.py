from flask import Flask
from .extentions import db, ma , jwt
from .routes.shop_routes import shop_bp
from .routes.products_route import product_bp
from .routes.cart_route import cart_bp
from .routes.auth_routes import auth_bp

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    # Register blueprints
    app.register_blueprint(shop_bp, url_prefix='/api/shops')
    app.register_blueprint(product_bp, url_prefix='/api/products')
    app.register_blueprint(cart_bp, url_prefix='/api/cart')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    return app
