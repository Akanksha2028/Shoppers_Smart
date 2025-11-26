
from database import db, app
from models.customer import Customer
from models.product import Product
from models.transaction import Transaction

with app.app_context():
    db.create_all()
    print("Database tables created successfully!")
