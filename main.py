import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
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

if __name__ == '__main__':
    app.run(debug=True)
