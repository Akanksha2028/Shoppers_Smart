from flask import Blueprint, request, jsonify
from database import db
from models.transaction import Transaction
from sqlalchemy.exc import IntegrityError

transaction_bp = Blueprint('transaction_bp', __name__)

@transaction_bp.route('/transactions', methods=['POST'])
def add_transaction():
    data = request.get_json()

    
    required_fields = ['customer_id', 'product_id', 'quantity']
    missing = [f for f in required_fields if f not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    new_t = Transaction(
        customer_id=data['customer_id'],
        product_id=data['product_id'],
        quantity=data['quantity']
    )

    try:
        db.session.add(new_t)
        db.session.commit()
        return jsonify({"message": "Transaction added successfully",
                        "transaction_id": new_t.transaction_id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({
            "error": "Invalid customer_id or product_id (foreign key error)."
        }), 400

@transaction_bp.route('/transactions', methods=['GET'])
def get_transactions():
    ts = Transaction.query.all()
    return jsonify([t.to_dict() for t in ts])

@transaction_bp.route('/transactions/<int:id>', methods=['GET'])
def get_transaction(id):
    t = Transaction.query.get(id)
    if not t:
        return jsonify({"error": "Transaction not found"}), 404
    return jsonify(t.to_dict())

@transaction_bp.route('/transactions/<int:id>', methods=['PUT'])
def update_transaction(id):
    t = Transaction.query.get(id)
    if not t:
        return jsonify({"error": "Transaction not found"}), 404

    data = request.get_json()

    if 'customer_id' in data:
        t.customer_id = data['customer_id']
    if 'product_id' in data:
        t.product_id = data['product_id']
    if 'quantity' in data:
        t.quantity = data['quantity']

    try:
        db.session.commit()
        return jsonify({"message": "Transaction updated successfully"})
    except IntegrityError:
        db.session.rollback()
        return jsonify({
            "error": "Invalid customer_id or product_id (foreign key error)."
        }), 400

@transaction_bp.route('/transactions/<int:id>', methods=['DELETE'])
def delete_transaction(id):
    t = Transaction.query.get(id)
    if not t:
        return jsonify({"error": "Transaction not found"}), 404

    db.session.delete(t)
    db.session.commit()
    return jsonify({"message": "Transaction deleted successfully"})

@transaction_bp.route('/by-product/<int:product_id>', methods=['DELETE'])
def delete_transactions_by_product(product_id):
    ts = Transaction.query.filter_by(product_id=product_id).all()
    if not ts:
        return jsonify({"message": "No transactions found for this product_id"}), 404

    for t in ts:
        db.session.delete(t)
    db.session.commit()

    return jsonify({
        "message": f"Deleted {len(ts)} transactions for product_id {product_id}"
    })