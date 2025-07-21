from flask import Blueprint, jsonify
import pickle
import os

router = Blueprint('recommendation_routes', __name__)

base_path = os.path.join(os.path.dirname(__file__), '..', 'recommender')

with open(os.path.join(base_path, 'customer_history.pkl'), 'rb') as f:
    customer_history = pickle.load(f)

with open(os.path.join(base_path, 'location_recommendations.pkl'), 'rb') as f:
    location_recommendations = pickle.load(f)

with open(os.path.join(base_path, 'pivot_table.pkl'), 'rb') as f:
    pivot_table = pickle.load(f)

with open(os.path.join(base_path, 'similarity.pkl'), 'rb') as f:
    similarity_matrix = pickle.load(f)

@router.route('/recommend/customer/<string:customer_id>', methods=['GET'])
def recommend_for_customer(customer_id):
    customer_id = str(customer_id)
    if customer_id not in pivot_table.index:
        return jsonify({"error": "customer not found"}), 404

    similar_users = similarity_matrix[customer_id].sort_values(ascending=False).drop(customer_id).head(10)
    recommended = {}

    for sim_user in similar_users.index:
        products = customer_history.get(str(sim_user), [])
        for product in products:
            recommended[product] = recommended.get(product, 0) + 1

    sorted_products = sorted(recommended.items(), key=lambda x: -x[1])
    return jsonify({
        "customer_id": customer_id,
        "recommendations": [product for product, _ in sorted_products[:5]]
    })

@router.route('/recommend/location/<string:location>', methods=['GET'])
def recommend_for_location(location):
    if location not in location_recommendations:
        return jsonify({"error": "location not found"}), 404

    return jsonify({
        "location": location,
        "top_products": location_recommendations[location]
    })

@router.route('/recommend/history/<string:customer_id>', methods=['GET'])
def customer_history_route(customer_id):
    customer_id = str(customer_id)
    if customer_id not in customer_history:
        return jsonify({"error": "customer not found"}), 404

    return jsonify({
        "customer_id": customer_id,
        "history": customer_history[customer_id]
    })


