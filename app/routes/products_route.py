from flask import Blueprint, request, jsonify
from app.extentions import db
from app.models import Product
from app.schemas import ProductSchema
from app.utils.jwt_auth import jwt_required_function

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('Getproducts/', methods=['GET'])
def get_products():
    products = Product.query.all()
    schema = ProductSchema(many=True)
    return jsonify(schema.dump(products))

@product_bp.route('Getproduct/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    schema = ProductSchema()
    return jsonify(schema.dump(product))

@product_bp.route('CreateProduct/', methods=['POST'])
@jwt_required_function
def create_product():
    data = request.json
    new_product = Product(name=data['name'], price=data['price'], shop_id=data['shop_id'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product created successfully"}), 201

@product_bp.route('EditProduct/<int:id>', methods=['PUT'])
@jwt_required_function
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.json
    product.name = data.get('name', product.name)
    product.price = data.get('price', product.price)
    db.session.commit()
    return jsonify({"message": "Product updated successfully"})

@product_bp.route('DeleteProduct/<int:id>', methods=['DELETE'])
@jwt_required_function
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully"})
