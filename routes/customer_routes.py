from flask import Blueprint, request, jsonify
from database import db
from models.customer import Customer
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func

customer_bp = Blueprint("customer_bp", __name__)

@customer_bp.route("/customers", methods=["GET"])
def get_customers():
    customers = Customer.query.all()
    result = []
    for c in customers:
        result.append({
            "customer_id": c.customer_id,
            "name": c.name,
            "email": c.email,
            "phone": c.phone_number,
            "location": c.location
        })
    return jsonify(result)


@customer_bp.route("/customers/<int:id>", methods=["GET"])
def get_customer(id):
    c = Customer.query.get(id)
    if not c:
        return jsonify({"error": "Customer not found"}), 404

    return jsonify({
        "customer_id": c.customer_id,
        "name": c.name,
        "email": c.email,
        "phone": c.phone_number,
        "location": c.location
    })


@customer_bp.route("/customers", methods=["POST"])
def add_customer():
    data = request.get_json() or {}

    name = data.get("name")
    email = data.get("email")
    location = data.get("location")
    phone = data.get("phone") or data.get("phone_number")

    if not name:
        return jsonify({"error": "name is required"}), 400

    customer_id = data.get("customer_id")
    if customer_id is None:
        max_id = db.session.query(func.max(Customer.customer_id)).scalar() or 0
        customer_id = max_id + 1

    new_customer = Customer(
        customer_id=customer_id,
        name=name,
        email=email,
        phone_number=phone,
        location=location
    )

    try:
        db.session.add(new_customer)
        db.session.commit()
        return jsonify({
            "message": "Customer added successfully",
            "customer": {
                "customer_id": new_customer.customer_id,
                "name": new_customer.name,
                "email": new_customer.email,
                "phone": new_customer.phone_number,
                "location": new_customer.location
            }
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@customer_bp.route("/customers/<int:id>", methods=["PUT"])
def update_customer(id):
    c = Customer.query.get(id)
    if not c:
        return jsonify({"error": "Customer not found"}), 404

    data = request.get_json() or {}

    if "name" in data:
        c.name = data["name"]
    if "email" in data:
        c.email = data["email"]
    if "location" in data:
        c.location = data["location"]
    if "phone" in data:
        c.phone_number = data["phone"]

    db.session.commit()
    return jsonify({"message": "Customer updated successfully"})

@customer_bp.route("/customers/<int:id>", methods=["DELETE"])
def delete_customer(id):
    c = Customer.query.get(id)
    if not c:
        return jsonify({"error": "Customer not found"}), 404

    try:
        db.session.delete(c)
        db.session.commit()
        return jsonify({"message": "Customer deleted successfully"})
    except IntegrityError:
        db.session.rollback()
        return jsonify({
            "error": "Cannot delete customer. There are transactions using this customer_id."
        }), 400
