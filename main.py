import sys
import os
import pickle

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, jsonify
import models.customers
import models.product
import models.transaction

from routes.customer_routes import router as customer_routes
from routes.product_routes import router as product_routes
from routes.transaction_routes import router as transaction_routes

from database import engine
from models import customers, product  
from database import Base

Base.metadata.create_all(bind=engine)

app = Flask(__name__)

app.register_blueprint(customer_routes)
app.register_blueprint(product_routes)
app.register_blueprint(transaction_routes)

@app.route('/')
def home():
    return "shopsmart API is working"

location_recommendation_path = os.path.join('ML_model/location_recommendation.pkl')

with open(location_recommendation_path, 'rb') as f:
    location_recommendations = pickle.load(f)

@app.route('/recommend/location/<string:location>', methods=['GET'])
def recommend_for_location(location):
    location = location.lower()
    available_locations = {loc.lower(): loc for loc in location_recommendations}

    if location not in available_locations:
        return jsonify({"error": "location not found"}), 404

    original_key = available_locations[location]
    return jsonify({
        "location": original_key,
        "top_products": location_recommendations[original_key]
    })

if __name__ == '__main__':
    app.run(debug=True)
