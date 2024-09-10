from flask import Blueprint, request, jsonify
from app.extentions import db
from app.models import Shop
from app.schemas import ShopSchema
from app.utils.jwt_auth import jwt_required_function

shop_bp = Blueprint('shop_bp', __name__)

@shop_bp.route('GetShop/', methods=['GET'])
def get_all_shops():  # Unique name
    shops = Shop.query.all()
    schema = ShopSchema(many=True)
    return jsonify(schema.dump(shops))

@shop_bp.route('SingleShop/<int:id>', methods=['GET'])
def get_single_shop(id):  # Unique name
    shop = Shop.query.get_or_404(id)
    schema = ShopSchema()
    return jsonify(schema.dump(shop))

@shop_bp.route('CreateShop/', methods=['POST'])
@jwt_required_function
def create_new_shop():  # Unique name
    data = request.json
    new_shop = Shop(name=data['name'], address=data['address'])
    db.session.add(new_shop)
    db.session.commit()
    return jsonify({"message": "Shop created successfully"}), 201

@shop_bp.route('EditShop/<int:id>', methods=['PUT'])
@jwt_required_function
def update_existing_shop(id):  # Unique name
    shop = Shop.query.get_or_404(id)
    data = request.json
    shop.name = data.get('name', shop.name)
    shop.address = data.get('address', shop.address)
    db.session.commit()
    return jsonify({"message": "Shop updated successfully"})

@shop_bp.route('DeleteShop/<int:id>', methods=['DELETE'])
@jwt_required_function
def delete_shop_by_id(id):  # Unique name
    shop = Shop.query.get_or_404(id)
    db.session.delete(shop)
    db.session.commit()
    return jsonify({"message": "Shop deleted successfully"})
