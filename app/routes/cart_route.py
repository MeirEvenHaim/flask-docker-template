from flask import Blueprint, request, jsonify
from app.extentions import db
from app.models import Cart
from app.schemas import CartSchema
from app.utils.jwt_auth import jwt_required_function

cart_bp = Blueprint('cart_bp', __name__)

@cart_bp.route('cart/', methods=['GET'])
@jwt_required_function
def get_cart_items():
    cart_items = Cart.query.all()
    schema = CartSchema(many=True)
    return jsonify(schema.dump(cart_items))

@cart_bp.route('CreateCart/', methods=['POST'])
@jwt_required_function
def add_to_cart():
    data = request.json
    new_cart_item = Cart(product_id=data['product_id'], user_id=data['user_id'], quantity=data['quantity'])
    db.session.add(new_cart_item)
    db.session.commit()
    return jsonify({"message": "Item added to cart successfully"}), 201

@cart_bp.route('DeleteCart/<int:id>', methods=['DELETE'])
@jwt_required_function
def remove_from_cart(id):
    cart_item = Cart.query.get_or_404(id)
    db.session.delete(cart_item)
    db.session.commit()
    return jsonify({"message": "Item removed from cart"})

@cart_bp.route('UpdateCart/<int:id>', methods=['PUT'])
@jwt_required_function
def update_cart_item(id):
    data = request.json
    cart_item = Cart.query.get_or_404(id)

    if 'quantity' in data:
        cart_item.quantity = data['quantity']

    db.session.commit()
    return jsonify({"message": "Cart item updated successfully"})