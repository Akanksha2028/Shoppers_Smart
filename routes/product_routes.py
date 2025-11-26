from flask import Blueprint, request, jsonify
from database import db
from models.product import Product
from sqlalchemy.exc import IntegrityError

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    product = Product(
        product_name=data['product_name'],
        description=data.get('description', ''),
        price=data['price']
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({"message": "Product added successfully"}), 201

@product_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products])

@product_bp.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    p = Product.query.get(id)
    if not p:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(p.to_dict())

@product_bp.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    p = Product.query.get(id)
    if not p:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json()
    if 'product_name' in data:
        p.product_name = data['product_name']
    if 'description' in data:
        p.description = data['description']
    if 'price' in data:
        p.price = data['price']

    db.session.commit()
    return jsonify({"message": "Product updated successfully"})


@product_bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    p = Product.query.get(id)
    if not p:
        return jsonify({"error": "Product not found"}), 404

    try:
        db.session.delete(p)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully"})
    except IntegrityError:
        db.session.rollback()
        return jsonify({
            "error": "Cannot delete product. There are transactions using this product_id."
        }), 400
