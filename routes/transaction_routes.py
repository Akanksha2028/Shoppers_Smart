import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Blueprint, request, jsonify
import mysql.connector
from models.transaction import Transaction
from database import SessionLocal

router = Blueprint('transaction', __name__)

@router.route("/transactions", methods=["POST"])
def add_transaction():
    db = SessionLocal()
    data = request.json
    new_transaction = Transaction(**data)
    db.add(new_transaction)
    db.commit()
    return jsonify({"message": "Transaction added"}), 201

@router.route("/transactions", methods=["GET"])
def get_transactions():
    db = SessionLocal()
    transactions = db.query(Transaction).all()
    return jsonify([t.__dict__ for t in transactions])

@router.route("/transactions/<int:id>", methods=["PUT"])
def update_transaction(id):
    db = SessionLocal()
    data = request.json
    transaction = db.query(Transaction).get(id)
    if not transaction:
        return jsonify({"message": "Not found"}), 404
    for key, value in data.items():
        setattr(transaction, key, value)
    db.commit()
    return jsonify({"message": "Transaction updated"})

@router.route("/transactions/<int:id>", methods=["DELETE"])
def delete_transaction(id):
    db = SessionLocal()
    transaction = db.query(Transaction).get(id)
    if not transaction:
        return jsonify({"message": "Not found"}), 404
    db.delete(transaction)
    db.commit()
    return jsonify({"message": "Transaction deleted"})
