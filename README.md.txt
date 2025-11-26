🛍️ ShopSmart – Location-Based Product Recommendation System

ShopSmart is a Flask + MySQL backend system that gives location-based product recommendations by analyzing customer purchase patterns.
It identifies top-selling products in a customer's area and recommends them intelligently.

🚀 Features
🔑 Customer Management

Add new customers

Update, delete, and retrieve customers

Validate customer via ID

📦 Product Management

Add, update, delete products

Fetch one or all products

Prevent product deletion if linked with transactions

💳 Transaction Management

Add new purchase transactions

Update/delete existing transactions

Fetch single or all transactions

📍 Location-Based Recommendations

Recommends products purchased most in the same location

Uses transaction analysis to determine popularity

📂 CSV Importer

Load CSV files directly into MySQL:

customers.csv

products.csv

transactions.csv

🔗 RESTful APIs

Clean structured API for:

Customers

Products

Transactions

Recommendations

🧪 Postman Tested

All endpoints tested with GET, POST, PUT, DELETE

🛠️ Tech Stack
Layer	Technology
Backend	Flask (Python)
Database	MySQL + SQLAlchemy ORM
Data Processing	Pandas
API Testing	Postman
Version Control	Git + GitHub
📂 Project Structure
ShoppersSmart/
│── main.py
│── database.py
│── csv_importer.py
│── recommender_utils.py
│── requirements.txt
│── .env
│
├── models/
│   ├── customer.py
│   ├── product.py
│   └── transaction.py
│
├── routes/
│   ├── customer_routes.py
│   ├── product_routes.py
│   ├── transaction_routes.py
│   └── recommendation_routes.py
│
├── data/
│   ├── customers.csv
│   ├── products.csv
│   └── transactions.csv
│
└── ShopSmartenv/    (ignored in .gitignore)

⚡ API Endpoints
👤 Customer APIs
Method	Endpoint	Description
POST	/customers	Add customer
GET	/customers	Get all customers
GET	/customers/<id>	Get customer by ID
PUT	/customers/<id>	Update customer
DELETE	/customers/<id>	Delete customer
📦 Product APIs
Method	Endpoint	Description
POST	/products	Add product
GET	/products	Get all products
GET	/products/<id>	Get product by ID
PUT	/products/<id>	Update product
DELETE	/products/<id>	Delete product (only if no transactions exist)
💳 Transaction APIs
Method	Endpoint	Description
POST	/transactions	Add transaction
GET	/transactions	Get all transactions
GET	/transactions/<id>	Get transaction by ID
PUT	/transactions/<id>	Update transaction
DELETE	/transactions/<id>	Delete transaction
🎯 Recommendation API
POST /recommend
Request:
{
  "customer_id": 251
}

Response Example:
{
  "location": "Pune",
  "recommended_products": [
    {
      "product_id": 23,
      "product_name": "TV",
      "total_purchases": 89
    }
  ]
}
