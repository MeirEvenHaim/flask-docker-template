from app import ma  # Import Marshmallow instance (ma)
from app.models import Shop, Product, Cart, User  # Import the SQLAlchemy models

# Shop Schema
class ShopSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Shop  # Reference the Shop model
        load_instance = True  # Deserialize to a model instance
        include_fk = True  # Include foreign keys in the schema if any

# Product Schema
class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product  # Reference the Product model
        load_instance = True  # Deserialize to a model instance
        include_fk = True  # Include foreign keys (shop_id) in the schema

# Cart Schema
class CartSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cart  # Reference the Cart model
        load_instance = True  # Deserialize to a model instance
        include_fk = True  # Include foreign keys (user_id, product_id) in the schema

# User Schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User  # Reference the User model
        load_instance = True  # Deserialize to a model instance
        include_fk = True  # Include foreign keys in the schema if any

# Optional: Separate schema for handling password hashing in registration and login
class UserRegistrationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

    password = ma.String(required=True, load_only=True)  # Prevent exposing the password
