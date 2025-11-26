from flask import Blueprint, jsonify
from recommender_utils import get_recommendations_by_location

recommend_bp = Blueprint('recommend_bp', __name__)

@recommend_bp.route('/recommend/<string:location>', methods=['GET'])
def recommend_by_location(location):
    result = get_recommendations_by_location(location)
    return jsonify(result)
