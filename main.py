from flask import jsonify
from database import app, db
from routes.customer_routes import customer_bp
from routes.product_routes import product_bp
from routes.transaction_routes import transaction_bp
from recommender_utils import get_recommendations_by_location
from flask import jsonify
from routes.recommendation_routes import recommend_bp

app.register_blueprint(recommend_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(product_bp)
app.register_blueprint(transaction_bp)

@app.route('/')
def home():
    return jsonify({"message": "ShopSmart Flask API is working"})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Render sets PORT env var
    app.run(host="0.0.0.0", port=port, debug=True)
